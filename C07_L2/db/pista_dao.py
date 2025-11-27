class PistaDAO:

    @staticmethod
    def insert(connection, pista):
        cursor = connection.cursor()
        query = """
            INSERT INTO Pista (nome, dificuldade) 
            VALUES (%s, %s)
        """
        cursor.execute(query, (pista['nome'], pista['dificuldade']))
        connection.commit()
        print(f"Pista {pista['nome']} inserida com sucesso.")

    @staticmethod
    def update(connection, id_pista, pista):
        cursor = connection.cursor()
        query = "UPDATE Pista SET "
        values = []

        if 'nome' in pista:
            query += "nome = %s, "
            values.append(pista['nome'])

        if 'dificuldade' in pista:
            query += "dificuldade = %s, "
            values.append(pista['dificuldade'])

        query = query.rstrip(', ') + " WHERE id_pista = %s"
        values.append(id_pista)

        cursor.execute(query, tuple(values))
        connection.commit()
        print(f"Pista de ID {id_pista} atualizada com sucesso.")

    @staticmethod
    def delete(connection, id_pista):
        cursor = connection.cursor()
        delete_pista_query = "DELETE FROM Pista WHERE id_pista = %s"
        cursor.execute(delete_pista_query, (id_pista,))
        connection.commit()
        print(f"Pista de ID {id_pista} deletada com sucesso.")

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Pista"
        cursor.execute(query)
        return cursor.fetchall()
