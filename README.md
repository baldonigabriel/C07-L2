# C07-L2
Projeto de C07

- Ideia do Projeto
  A ideia foi inspirada no Mário Kart, onde jogadores podem escolher personagens, karts e disputar corridas em diferentes pistas.
  O sistema também permite registrar os resultados das corridas e as conquistas desbloqueadas por cada jogador.

- Entidades

Jogador, Personagem, Kart, Pista, Corrida e Conquista

- Relacionamentos

Jogador 1:1 Personagem → Cada jogador escolhe um personagem único.

Jogador 1:N Kart → Um jogador pode possuir vários karts.

Jogador N:M Corrida → Jogadores participam de várias corridas, e cada corrida tem vários jogadores.

Corrida 1:N Pista → Cada corrida ocorre em uma pista, mas uma pista pode receber várias corridas.

Jogador N:M Conquista → Jogadores podem desbloquear várias conquistas, e cada conquista pode ser desbloqueada por vários jogadores.
