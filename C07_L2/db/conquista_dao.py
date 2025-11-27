class ConquistaDAO:

    @staticmethod
    def insert(connection, conquista):
        cursor = connection.cursor()
        query = """
            INSERT INTO Conquista (descricao, nome) 
            VALUES (%s, %s)
        """
        cursor.execute(query, (conquista['descricao'], conquista['nome']))
        connection.commit()
        print(f"Conquista {conquista['nome']} inserida com sucesso.")

    @staticmethod
    def update(connection, id_conquista, conquista):
        cursor = connection.cursor()
        query = "UPDATE Conquista SET "
        values = []

        if 'descricao' in conquista:
            query += "descricao = %s, "
            values.append(conquista['descricao'])

        if 'nome' in conquista:
            query += "nome = %s, "
            values.append(conquista['nome'])

        query = query.rstrip(', ') + " WHERE id_conquista = %s"
        values.append(id_conquista)

        cursor.execute(query, tuple(values))
        connection.commit()
        print(f"Conquista de ID {id_conquista} atualizada com sucesso.")

    @staticmethod
    def delete(connection, id_conquista):
        cursor = connection.cursor()
        delete_conquista_query = "DELETE FROM Conquista WHERE id_conquista = %s"
        cursor.execute(delete_conquista_query, (id_conquista,))
        connection.commit()
        print(f"Conquista de ID {id_conquista} deletada com sucesso.")

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Conquista"
        cursor.execute(query)
        return cursor.fetchall()
