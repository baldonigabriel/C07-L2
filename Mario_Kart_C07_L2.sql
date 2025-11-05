CREATE DATABASE IF NOT EXISTS c07_mk;
USE c07_mk;

DROP TABLE IF EXISTS Jogador_has_Conquista;
DROP TABLE IF EXISTS Corrida_has_Jogador;
DROP TABLE IF EXISTS Jogador;
DROP TABLE IF EXISTS Personagem;
DROP TABLE IF EXISTS Conquista;
DROP TABLE IF EXISTS Kart;
DROP TABLE IF EXISTS Pista;
DROP TABLE IF EXISTS Corrida;

CREATE TABLE Personagem (
    idPersonagem INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45),
    habilidade_especial VARCHAR(45)
);

CREATE TABLE Jogador (
    idJogador INT AUTO_INCREMENT PRIMARY KEY,
    nick_name VARCHAR(45),
    Personagem_idPersonagem INT,
    FOREIGN KEY (Personagem_idPersonagem) REFERENCES Personagem(idPersonagem)
);

CREATE TABLE Conquista (
    id_conquista INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(45),
    nome VARCHAR(45)
);

CREATE TABLE Jogador_has_Conquista (
    Jogador_idJogador INT,
    Jogador_Personagem_idPersonagem INT,
    Conquista_id_conquista INT,
    PRIMARY KEY (Jogador_idJogador, Jogador_Personagem_idPersonagem, Conquista_id_conquista),
    FOREIGN KEY (Jogador_idJogador) REFERENCES Jogador(idJogador),
    FOREIGN KEY (Jogador_Personagem_idPersonagem) REFERENCES Personagem(idPersonagem),
    FOREIGN KEY (Conquista_id_conquista) REFERENCES Conquista(id_conquista)
);

CREATE TABLE Pista (
    id_pista INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45),
    dificuldade VARCHAR(45)
);

CREATE TABLE Corrida (
    id_corrida INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(45),
    tempo_total VARCHAR(45)
);

CREATE TABLE Corrida_has_Jogador (
    Corrida_id_corrida INT,
    Jogador_idJogador INT,
    PRIMARY KEY (Corrida_id_corrida, Jogador_idJogador),
    FOREIGN KEY (Corrida_id_corrida) REFERENCES Corrida(id_corrida),
    FOREIGN KEY (Jogador_idJogador) REFERENCES Jogador(idJogador)
);

CREATE TABLE Kart (
    id_Kart INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(45),
    velocidade_max DOUBLE,
    Jogador_idJogador INT,
    Jogador_Personagem_idPersonagem INT,
    FOREIGN KEY (Jogador_idJogador) REFERENCES Jogador(idJogador),
    FOREIGN KEY (Jogador_Personagem_idPersonagem) REFERENCES Personagem(idPersonagem)
);

INSERT INTO Personagem (nome, habilidade_especial) VALUES
('Mario', 'Super Pulo'),
('Peach', 'Flores Mágicas'),
('Bowser', 'Força Bruta');

INSERT INTO Jogador (nick_name, Personagem_idPersonagem) VALUES
('Speedy', 1),
('QueenP', 2),
('KoopaKing', 3);

INSERT INTO Conquista (descricao, nome) VALUES
('Venceu a primeira corrida', 'Primeira Vitória'),
('Fez uma volta rápida', 'Velocista'),
('Completou 10 corridas', 'Maratonista');

INSERT INTO Jogador_has_Conquista (Jogador_idJogador, Jogador_Personagem_idPersonagem, Conquista_id_conquista) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

INSERT INTO Pista (nome, dificuldade) VALUES
('Circuito Cogumelo', 'Média'),
('Castelo Bowser', 'Difícil'),
('Pista Arco-Íris', 'Muito Difícil');

INSERT INTO Corrida (data, tempo_total) VALUES
('2025-11-01', '00:30:45'),
('2025-11-02', '00:28:20'),
('2025-11-03', '00:32:10');

INSERT INTO Corrida_has_Jogador (Corrida_id_corrida, Jogador_idJogador) VALUES
(1, 1),
(1, 2),
(2, 2),
(2, 3),
(3, 3),
(3, 1);

INSERT INTO Kart (modelo, velocidade_max, Jogador_idJogador, Jogador_Personagem_idPersonagem) VALUES
('Standard', 120.00, 1, 1),
('Mach Bike', 130.00, 2, 2),
('Flame Runner', 140.00, 3, 3);

ALTER TABLE Kart ADD COLUMN ano_modelo INT DEFAULT 2020;

CREATE VIEW view_pontuacao AS
SELECT j.nick_name AS jogador, SUM(c.id_corrida) AS total_corridas
FROM Jogador j
JOIN Corrida_has_Jogador c ON c.Jogador_idJogador = j.idJogador
GROUP BY j.nick_name;

SELECT * FROM view_pontuacao;
