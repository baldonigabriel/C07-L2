class PistaDAO:

    @staticmethod
    def insert(connection, pista):
        cursor = connection.cursor()
        query = "INSERT INTO Pista (nome, dificuldade) VALUES (%s, %s)"
        cursor.execute(query, (pista['nome'], pista['dificuldade']))
        connection.commit()

    @staticmethod
    def update(connection, id_pista, pista):
        cursor = connection.cursor()
        query = "UPDATE Pista SET nome = %s, dificuldade = %s WHERE id_pista = %s"
        cursor.execute(query, (pista['nome'], pista['dificuldade'], id_pista))
        connection.commit()

    @staticmethod
    def delete(connection, id_pista):
        cursor = connection.cursor()
        query = "DELETE FROM Pista WHERE id_pista = %s"
        cursor.execute(query, (id_pista,))
        connection.commit()

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Pista"
        cursor.execute(query)
        return cursor.fetchall()
