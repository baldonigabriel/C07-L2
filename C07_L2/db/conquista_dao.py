class ConquistaDAO:

    @staticmethod
    def insert(connection, conquista):
        cursor = connection.cursor()
        query = "INSERT INTO Conquista (descricao, nome) VALUES (%s, %s)"
        cursor.execute(query, (conquista['descricao'], conquista['nome']))
        connection.commit()

    @staticmethod
    def update(connection, id_conquista, conquista):
        cursor = connection.cursor()
        query = "UPDATE Conquista SET descricao = %s, nome = %s WHERE id_conquista = %s"
        cursor.execute(query, (conquista['descricao'], conquista['nome'], id_conquista))
        connection.commit()

    @staticmethod
    def delete(connection, id_conquista):
        cursor = connection.cursor()
        query = "DELETE FROM Conquista WHERE id_conquista = %s"
        cursor.execute(query, (id_conquista,))
        connection.commit()

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Conquista"
        cursor.execute(query)
        return cursor.fetchall()
