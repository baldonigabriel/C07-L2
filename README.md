# C07-L2
Projeto de C07

- Ideia do Projeto
  Este projeto tem como objetivo modelar um sistema inspirado no Mario Kart, onde jogadores podem escolher personagens, karts e disputar corridas em diferentes pistas.
  O sistema também permite registrar os resultados das corridas e as conquistas desbloqueadas por cada jogador.

- Entidades

Jogador
id_jogador (PK)
nickname
id_personagem (FK → Personagem)

Personagem
id_personagem (PK)
nome
habilidade_especial

Kart
id_kart (PK)
modelo
velocidade_max
id_jogador (FK → Jogador)

Pista
id_pista (PK)
nome
dificuldade

Corrida
id_corrida (PK)
data
id_pista (FK → Pista)

Conquista
id_conquista (PK)
nome
descricao

Participação Corrida (tabela de junção Jogador ↔ Corrida)
id_corrida (FK → Corrida)
id_jogador (FK → Jogador)
id_kart (FK → Kart)
posicao
tempo_total
melhor_volta
pontos

Jogador Conquista (tabela de junção Jogador ↔ Conquista)
id_jogador (FK → Jogador)
id_conquista (FK → Conquista)
data_conquista

- Relacionamentos

Jogador 1:1 Personagem → Cada jogador escolhe um personagem único.
Jogador 1:N Kart → Um jogador pode possuir vários karts.
Jogador N:M Corrida → Jogadores participam de várias corridas, e cada corrida tem vários jogadores.
Corrida 1:N Pista → Cada corrida ocorre em uma pista, mas uma pista pode receber várias corridas.
Jogador N:M Conquista → Jogadores podem desbloquear várias conquistas, e cada conquista pode ser desbloqueada por vários jogadores (tabela Jogador Conquista).
