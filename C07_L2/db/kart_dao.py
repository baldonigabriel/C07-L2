class KartDAO:

    @staticmethod
    def insert(connection, kart):
        cursor = connection.cursor()
        query = "INSERT INTO Kart (Modelo, velocidade_max, Jogador_idJogador) VALUES (%s, %s, %s)"
        cursor.execute(query, (kart['Modelo'], kart['velocidade_max'], kart['Jogador_idJogador']))
        connection.commit()

    @staticmethod
    def update(connection, id_kart, kart):
        cursor = connection.cursor()
        query = "UPDATE Kart SET Modelo = %s, velocidade_max = %s WHERE id_Kart = %s"
        cursor.execute(query, (kart['Modelo'], kart['velocidade_max'], id_kart))
        connection.commit()

    @staticmethod
    def delete(connection, id_kart):
        cursor = connection.cursor()
        query = "DELETE FROM Kart WHERE id_Kart = %s"
        cursor.execute(query, (id_kart,))
        connection.commit()

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Kart"
        cursor.execute(query)
        return cursor.fetchall()
