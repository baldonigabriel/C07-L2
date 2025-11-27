class JogadorDAO:

    @staticmethod
    def insert(connection, jogador):
        cursor = connection.cursor()
        query = """
            INSERT INTO Jogador (nick_name, Personagem_idPersonagem, idade) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (jogador['nick_name'], jogador['Personagem_idPersonagem'], jogador['idade']))
        connection.commit()
        print(f"Jogador {jogador['nick_name']} inserido com sucesso.")

    @staticmethod
    def update(connection, id_jogador, jogador):
        cursor = connection.cursor()
        query = "UPDATE Jogador SET "
        values = []

        if 'nick_name' in jogador:
            query += "nick_name = %s, "
            values.append(jogador['nick_name'])

        if 'Personagem_idPersonagem' in jogador:
            query += "Personagem_idPersonagem = %s, "
            values.append(jogador['Personagem_idPersonagem'])

        if 'idade' in jogador:
            query += "idade = %s, "
            values.append(jogador['idade'])

        query = query.rstrip(', ') + " WHERE idJogador = %s"
        values.append(id_jogador)

        cursor.execute(query, tuple(values))
        connection.commit()
        print(f"Jogador de ID {id_jogador} atualizado com sucesso.")

    @staticmethod
    def delete(connection, id_jogador):
        cursor = connection.cursor()
        delete_jogador_query = "DELETE FROM Jogador WHERE idJogador = %s"
        cursor.execute(delete_jogador_query, (id_jogador,))
        connection.commit()
        print(f"Jogador de ID {id_jogador} deletado com sucesso.")

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Jogador"
        cursor.execute(query)
        return cursor.fetchall()
