CREATE TABLE Personagem (
    idPersonagem INT PRIMARY KEY,
    Nome VARCHAR(45),
    habilidade_especial VARCHAR(45)
);

CREATE TABLE Jogador (
    idJogador INT PRIMARY KEY,
    nick_name VARCHAR(45),
    Personagem_idPersonagem INT,
    FOREIGN KEY (Personagem_idPersonagem) REFERENCES Personagem(idPersonagem)
);

CREATE TABLE Kart (
    id_Kart INT PRIMARY KEY,
    Modelo VARCHAR(45),
    velocidade_max DOUBLE,
    Jogador_idJogador INT,
    FOREIGN KEY (Jogador_idJogador) REFERENCES Jogador(idJogador)
);

CREATE TABLE Pista (
    id_pista INT PRIMARY KEY,
    nome VARCHAR(45),
    dificuldade VARCHAR(45)
);

CREATE TABLE Corrida (
    id_corrida INT PRIMARY KEY,
    data VARCHAR(45),
    tempo_total VARCHAR(45),
    Corrida_id_pista INT,
    FOREIGN KEY (Corrida_id_pista) REFERENCES Pista(id_pista)
);

CREATE TABLE Conquista (
    id_conquista INT PRIMARY KEY,
    descricao VARCHAR(45),
    nome VARCHAR(45)
);

CREATE TABLE Corrida_has_Jogador (
    Corrida_id_corrida INT,
    Jogador_idJogador INT,
    PRIMARY KEY (Corrida_id_corrida, Jogador_idJogador),
    FOREIGN KEY (Corrida_id_corrida) REFERENCES Corrida(id_corrida),
    FOREIGN KEY (Jogador_idJogador) REFERENCES Jogador(idJogador)
);

CREATE TABLE Jogador_has_Conquista (
    Jogador_idJogador INT,
    Conquista_id_conquista INT,
    PRIMARY KEY (Jogador_idJogador, Conquista_id_conquista),
    FOREIGN KEY (Jogador_idJogador) REFERENCES Jogador(idJogador),
    FOREIGN KEY (Conquista_id_conquista) REFERENCES Conquista(id_conquista)
);

INSERT INTO Personagem (idPersonagem, Nome, habilidade_especial) VALUES
(1, 'Mario', 'Super Pulo'),
(2, 'Luigi', 'Super Força'),
(3, 'Peach', 'Golpe de Flor'),
(4, 'Yoshi', 'Super Salto'),
(5, 'Bowser', 'Super Defesa');

INSERT INTO Jogador (idJogador, nick_name, Personagem_idPersonagem) VALUES
(1, 'Player1', 1),
(2, 'Player2', 2),
(3, 'Player3', 3),
(4, 'Player4', 4),
(5, 'Player5', 5);

INSERT INTO Kart (id_Kart, Modelo, velocidade_max, Jogador_idJogador) VALUES
(1, 'Mach 8', 150.0, 1),
(2, 'Flame Rider', 145.0, 2),
(3, 'Standard Kart', 140.0, 3),
(4, 'Pipe Frame', 130.0, 4),
(5, 'Sneakster', 135.0, 5);

INSERT INTO Pista (id_pista, nome, dificuldade) VALUES
(1, 'Circuito Donkey Kong', 'Fácil'),
(2, 'Pista Rainbow', 'Média'),
(3, 'Pista Bowser', 'Difícil'),
(4, 'Pista Toad Circuit', 'Média'),
(5, 'Pista Wario Shipyard', 'Difícil');

INSERT INTO Corrida (id_corrida, data, tempo_total, Corrida_id_pista) VALUES
(1, '2023-10-01', '00:05:00', 1),
(2, '2023-10-02', '00:10:00', 2),
(3, '2023-10-03', '00:15:00', 3),
(4, '2023-10-04', '00:12:00', 4),
(5, '2023-10-05', '00:08:00', 5);

INSERT INTO Conquista (id_conquista, descricao, nome) VALUES
(1, 'Venceu o Circuito Donkey Kong', 'Vencedor DK'),
(2, 'Venceu a Pista Rainbow', 'Vencedor Rainbow'),
(3, 'Venceu a Pista Bowser', 'Vencedor Bowser'),
(4, 'Venceu a Pista Toad Circuit', 'Vencedor Toad'),
(5, 'Venceu a Pista Wario Shipyard', 'Vencedor Wario');

INSERT INTO Corrida_has_Jogador (Corrida_id_corrida, Jogador_idJogador) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO Jogador_has_Conquista (Jogador_idJogador, Conquista_id_conquista) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

UPDATE Personagem SET Nome = 'Mario Kart' WHERE idPersonagem = 1;
UPDATE Kart SET Modelo = 'Mach 8 (Mario)' WHERE id_Kart = 1;

DELETE FROM Corrida WHERE id_corrida = 3;
DELETE FROM Jogador WHERE idJogador = 2;

ALTER TABLE Jogador ADD COLUMN idade INT AFTER nick_name;

DROP TABLE IF EXISTS Conquista;

CREATE USER 'mario_usuario'@'localhost' IDENTIFIED BY 'senha_secreta';
GRANT ALL PRIVILEGES ON *.* TO 'mario_usuario'@'localhost' WITH GRANT OPTION;

CREATE VIEW ViewJogadoresConquistas AS
SELECT Jogador.nick_name, COUNT(Conquista.id_conquista) AS numero_conquistas
FROM Jogador
JOIN Jogador_has_Conquista ON Jogador.idJogador = Jogador_has_Conquista.Jogador_idJogador
JOIN Conquista ON Jogador_has_Conquista.Conquista_id_conquista = Conquista.id_conquista
GROUP BY Jogador.idJogador;

DELIMITER //

CREATE TRIGGER before_insert_corrida
BEFORE INSERT ON Corrida
FOR EACH ROW
BEGIN
    SET NEW.tempo_total = TIMESTAMPDIFF(SECOND, '00:00:00', NEW.tempo_total);
END //

DELIMITER ;


DELIMITER //

CREATE FUNCTION calcular_media_tempo_corrida()
RETURNS DOUBLE
DETERMINISTIC
BEGIN
    DECLARE media_tempo DOUBLE;
    SELECT AVG(TIMESTAMPDIFF(SECOND, '00:00:00', tempo_total)) INTO media_tempo FROM Corrida;
    RETURN media_tempo;
END //

DELIMITER ;
