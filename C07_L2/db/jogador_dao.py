class JogadorDAO:

    @staticmethod
    def insert(connection, jogador):
        cursor = connection.cursor()
        query = "INSERT INTO Jogador (nick_name, Personagem_idPersonagem) VALUES (%s, %s)"
        cursor.execute(query, (jogador['nick_name'], jogador['Personagem_idPersonagem']))
        connection.commit()
        print(f"Jogador {jogador['nick_name']} inserido com sucesso.")

    @staticmethod
    def update(connection, id_jogador, jogador):
        cursor = connection.cursor()
        query = "UPDATE Jogador SET nick_name = %s WHERE idJogador = %s"
        cursor.execute(query, (jogador['nick_name'], id_jogador))
        connection.commit()

    @staticmethod
    def delete(connection, id_jogador):
        cursor = connection.cursor()

        # Excluir o jogador da tabela Jogador. O MySQL cuidará das referências automaticamente.
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
