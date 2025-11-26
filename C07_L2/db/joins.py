# Em db/joins.py

def select_players_with_characters(connection):
    cursor = connection.cursor()
    query = """
        SELECT Jogador.nick_name, Personagem.Nome
        FROM Jogador
        JOIN Personagem ON Jogador.Personagem_idPersonagem = Personagem.idPersonagem
    """
    cursor.execute(query)
    return cursor.fetchall()

def select_karts_with_players(connection):
    cursor = connection.cursor()
    query = """
        SELECT Kart.Modelo, Jogador.nick_name
        FROM Kart
        JOIN Jogador ON Kart.Jogador_idJogador = Jogador.idJogador
    """
    cursor.execute(query)
    return cursor.fetchall()  # Retorna uma lista de tuplas

def select_races_with_tracks(connection):
    cursor = connection.cursor()
    query = """
        SELECT Corrida.id_corrida, Pista.nome
        FROM Corrida
        JOIN Pista ON Corrida.Corrida_id_pista = Pista.id_pista
    """
    cursor.execute(query)
    return cursor.fetchall()  # Retorna uma lista de tuplas

def select_players_with_conquests(connection):
    cursor = connection.cursor()
    query = """
        SELECT Jogador.nick_name, Conquista.nome
        FROM Jogador
        JOIN Jogador_has_Conquista ON Jogador.idJogador = Jogador_has_Conquista.Jogador_idJogador
        JOIN Conquista ON Jogador_has_Conquista.Conquista_id_conquista = Conquista.id_conquista
    """
    cursor.execute(query)
    return cursor.fetchall()  # Retorna uma lista de tuplas

def select_races_with_players(connection):
    cursor = connection.cursor()
    query = """
        SELECT Corrida.id_corrida, Jogador.nick_name
        FROM Corrida
        JOIN Corrida_has_Jogador ON Corrida.id_corrida = Corrida_has_Jogador.Corrida_id_corrida
        JOIN Jogador ON Corrida_has_Jogador.Jogador_idJogador = Jogador.idJogador
    """
    cursor.execute(query)
    return cursor.fetchall()  # Retorna uma lista de tuplas

def select_karts_with_conquests(connection):
    cursor = connection.cursor()
    query = """
        SELECT Kart.Modelo, Conquista.nome
        FROM Kart
        JOIN Jogador ON Kart.Jogador_idJogador = Jogador.idJogador
        JOIN Jogador_has_Conquista ON Jogador.idJogador = Jogador_has_Conquista.Jogador_idJogador
        JOIN Conquista ON Jogador_has_Conquista.Conquista_id_conquista = Conquista.id_conquista
    """
    cursor.execute(query)
    return cursor.fetchall()  # Retorna uma lista de tuplas
