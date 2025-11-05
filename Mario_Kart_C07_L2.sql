CREATE TABLE personagem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL UNIQUE,
    categoria VARCHAR(30) NOT NULL  -- leve, medio, pesado
);

CREATE TABLE jogador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(40) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    personagem_id INT NOT NULL,
    total_pontos INT NOT NULL DEFAULT 0,
    CONSTRAINT fk_jogador_personagem FOREIGN KEY (personagem_id) REFERENCES personagem(id)
);

CREATE TABLE kart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(60) NOT NULL,
    velocidade_max DECIMAL(5,2) NOT NULL, -- km/h
    aceleracao DECIMAL(5,2) NOT NULL,     -- m/s^2
    jogador_id INT NOT NULL,
    CONSTRAINT fk_kart_jogador FOREIGN KEY (jogador_id) REFERENCES jogador(id)
);

CREATE TABLE pista (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL UNIQUE,
    localidade VARCHAR(60) NOT NULL,
    extensao_km DECIMAL(5,2) NOT NULL
);

CREATE TABLE corrida (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pista_id INT NOT NULL,
	data_corrida DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_corrida_pista FOREIGN KEY (pista_id) REFERENCES pista(id)
);

-- Jogador N:M Corrida (participações e resultados)
CREATE TABLE participacao (
    corrida_id INT NOT NULL,
    jogador_id INT NOT NULL,
    posicao INT NOT NULL,
    tempo_seg DECIMAL(8,3) NOT NULL,
    pontos INT NOT NULL DEFAULT 0,
    PRIMARY KEY (corrida_id, jogador_id),
    CONSTRAINT fk_participacao_corrida FOREIGN KEY (corrida_id) REFERENCES corrida(id) ON DELETE CASCADE,
    CONSTRAINT fk_participacao_jogador FOREIGN KEY (jogador_id) REFERENCES jogador(id) ON DELETE CASCADE
    -- Observação: CHECKs são suportados no MySQL 8.0+; omitidos por compatibilidade ampla
);

-- Conquistas e ligação N:M com Jogador
CREATE TABLE conquista (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL UNIQUE,
    descricao TEXT
);

CREATE TABLE jogador_conquista (
    jogador_id INT NOT NULL,
    conquista_id INT NOT NULL,
    desbloqueada_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (jogador_id, conquista_id),
    CONSTRAINT fk_jc_jogador FOREIGN KEY (jogador_id) REFERENCES jogador(id) ON DELETE CASCADE,
    CONSTRAINT fk_jc_conquista FOREIGN KEY (conquista_id) REFERENCES conquista(id) ON DELETE CASCADE
);

-- =====================
-- Inserts de amostragem
-- =====================

INSERT INTO personagem (nome, categoria) VALUES
('Mario', 'medio'),
('Peach', 'leve'),
('Bowser', 'pesado');

INSERT INTO jogador (nickname, email, personagem_id) VALUES
('Speedy', 'speedy@example.com', 1),
('QueenP', 'queenp@example.com', 2),
('KoopaKing', 'koopaking@example.com', 3);

INSERT INTO kart (modelo, velocidade_max, aceleracao, jogador_id) VALUES
('Standard Kart', 120.00, 3.50, 1),
('Mach Bike',    140.00, 3.20, 2),
('Flame Runner', 150.00, 3.00, 3);

INSERT INTO pista (nome, localidade, extensao_km) VALUES
('Circuito Cogumelo', 'Reino Cogumelo', 3.20),
('Castelo do Bowser', 'Reino Koopa',    4.80),
('Pista Arco-Íris',   'Espaço',         6.00);

INSERT INTO corrida (pista_id, data_corrida) VALUES
(1, CURRENT_DATE - INTERVAL 2 DAY),
(2, CURRENT_DATE - INTERVAL 1 DAY),
(3, CURRENT_DATE);

INSERT INTO conquista (nome, descricao) VALUES
('Primeira Vitória', 'Ganhou a primeira corrida'),
('Velocista',        'Terminou uma corrida com média > 120 km/h'),
('Maratonista',      'Participou de 10 corridas');

INSERT INTO participacao (corrida_id, jogador_id, posicao, tempo_seg, pontos) VALUES
(1, 1, 1, 180.321, 15),
(1, 2, 2, 184.555, 10),
(1, 3, 3, 190.010, 8),
(2, 2, 1, 240.777, 15),
(2, 3, 2, 245.333, 10),
(2, 1, 3, 249.999, 8),
(3, 3, 1, 310.555, 15),
(3, 1, 2, 312.111, 10),
(3, 2, 3, 315.000, 8);

INSERT INTO jogador_conquista (jogador_id, conquista_id) VALUES
(1, 1),
(2, 1),
(3, 1);

-- ============================================
-- ALTER (exigência): adicionando coluna opcional
-- ============================================
ALTER TABLE kart ADD COLUMN ano_modelo INT DEFAULT 2020;

-- ============================================
-- VIEW #1: Ranking por pista (média e soma)
-- ============================================
DROP VIEW IF EXISTS v_ranking_pista;
CREATE VIEW v_ranking_pista AS
SELECT
    c.pista_id,
    p.nome AS pista,
    j.id   AS jogador_id,
    j.nickname,
    ROUND(AVG(pa.pontos), 2) AS media_pontos,
    SUM(pa.pontos) AS soma_pontos
FROM corrida c
JOIN participacao pa ON pa.corrida_id = c.id
JOIN jogador j ON j.id = pa.jogador_id
JOIN pista p ON p.id = c.pista_id
GROUP BY c.pista_id, p.nome, j.id, j.nickname;

-- ============================
-- FUNCTION #1: média de pontos
-- ============================
DELIMITER //
CREATE FUNCTION fn_media_pontos_jogador(p_jogador_id INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE m DECIMAL(10,2);
    SELECT IFNULL(AVG(pontos), 0) INTO m
    FROM participacao
    WHERE jogador_id = p_jogador_id;
    RETURN m;
END//
DELIMITER ;

-- =========================================
-- TRIGGERS: manter jogador.total_pontos
-- =========================================
DELIMITER //

CREATE TRIGGER tg_total_pontos_ins
AFTER INSERT ON participacao
FOR EACH ROW
BEGIN
    UPDATE jogador j
    SET total_pontos = (
        SELECT IFNULL(SUM(pontos),0) FROM participacao p
        WHERE p.jogador_id = NEW.jogador_id
    )
    WHERE j.id = NEW.jogador_id;
END//

CREATE TRIGGER tg_total_pontos_upd
AFTER UPDATE ON participacao
FOR EACH ROW
BEGIN
    -- Recalcula para o jogador atual:
    UPDATE jogador j
    SET total_pontos = (
        SELECT IFNULL(SUM(pontos),0) FROM participacao p
        WHERE p.jogador_id = NEW.jogador_id
    )
    WHERE j.id = NEW.jogador_id;

    -- Se o jogador mudou, também recalcula para o antigo:
    IF (OLD.jogador_id <> NEW.jogador_id) THEN
        UPDATE jogador j
        SET total_pontos = (
            SELECT IFNULL(SUM(pontos),0) FROM participacao p
            WHERE p.jogador_id = OLD.jogador_id
        )
        WHERE j.id = OLD.jogador_id;
    END IF;
END//

CREATE TRIGGER tg_total_pontos_del
AFTER DELETE ON participacao
FOR EACH ROW
BEGIN
    UPDATE jogador j
    SET total_pontos = (
        SELECT IFNULL(SUM(pontos),0) FROM participacao p
        WHERE p.jogador_id = OLD.jogador_id
    )
    WHERE j.id = OLD.jogador_id;
END//

DELIMITER ;

-- Disparo inicial (popular total_pontos para dados já inseridos)
UPDATE jogador j
SET total_pontos = (
    SELECT IFNULL(SUM(pontos),0) FROM participacao p WHERE p.jogador_id = j.id
);

-- =====================================
-- PROCEDURE #1: registrar participação
-- =====================================
DELIMITER //
CREATE PROCEDURE sp_registrar_participacao(
    IN p_corrida_id INT,
    IN p_jogador_id INT,
    IN p_posicao INT,
    IN p_tempo_seg DECIMAL(8,3),
    IN p_pontos INT
)
BEGIN
    INSERT INTO participacao (corrida_id, jogador_id, posicao, tempo_seg, pontos)
    VALUES (p_corrida_id, p_jogador_id, p_posicao, p_tempo_seg, p_pontos);
END//
DELIMITER ;

-- ===============================
-- Demonstrações de uso
-- ===============================

-- 1) Usar a VIEW
SELECT * FROM v_ranking_pista ORDER BY pista_id, soma_pontos DESC;

-- 2) Usar a FUNCTION
SELECT j.nickname, fn_media_pontos_jogador(j.id) AS media
FROM jogador j
ORDER BY media DESC;

-- 3) Usar a PROCEDURE (insere nova participação)
CALL sp_registrar_participacao(1, 1, 4, 200.000, 5);
SELECT nickname, total_pontos FROM jogador ORDER BY total_pontos DESC;

-- =================================================
-- UPDATE e DELETE "totais"
-- =================================================

-- UPDATE total: aumentar todas as velocidades em 5%
UPDATE kart SET velocidade_max = velocidade_max * 1.05;

-- DELETE total: criar e apagar uma tabela de log
CREATE TABLE IF NOT EXISTS log_temp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    msg TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO log_temp (msg) VALUES ('Carga inicial'), ('Teste de remoção'), ('Outro registro');
DELETE FROM log_temp;
DROP TABLE IF EXISTS log_temp;

-- =============================================
-- Usuário de SGBD com privilégios (MySQL)
-- =============================================
-- Execute como usuário com permissão de administração
CREATE USER IF NOT EXISTS 'mk_user'@'localhost' IDENTIFIED BY 'mk_password';
-- Troque c07_mk pelo nome do seu banco antes de rodar:
-- GRANTS para o schema inteiro
GRANT SELECT, INSERT, UPDATE, DELETE ON c07_mk.* TO 'mk_user'@'localhost';
FLUSH PRIVILEGES;

-- FIM
