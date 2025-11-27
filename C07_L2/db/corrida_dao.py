class CorridaDAO:

    @staticmethod
    def insert(connection, corrida):
        cursor = connection.cursor()
        query = """
            INSERT INTO Corrida (data, tempo_total, Corrida_id_pista) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (corrida['data'], corrida['tempo_total'], corrida['Corrida_id_pista']))
        connection.commit()
        print(f"Corrida em {corrida['data']} inserida com sucesso.")

    @staticmethod
    def update(connection, id_corrida, corrida):
        cursor = connection.cursor()
        query = "UPDATE Corrida SET "
        values = []

        if 'data' in corrida:
            query += "data = %s, "
            values.append(corrida['data'])

        if 'tempo_total' in corrida:
            query += "tempo_total = %s, "
            values.append(corrida['tempo_total'])

        if 'Corrida_id_pista' in corrida:
            query += "Corrida_id_pista = %s, "
            values.append(corrida['Corrida_id_pista'])

        query = query.rstrip(', ') + " WHERE id_corrida = %s"
        values.append(id_corrida)

        cursor.execute(query, tuple(values))
        connection.commit()
        print(f"Corrida de ID {id_corrida} atualizada com sucesso.")

    @staticmethod
    def delete(connection, id_corrida):
        cursor = connection.cursor()
        delete_corrida_query = "DELETE FROM Corrida WHERE id_corrida = %s"
        cursor.execute(delete_corrida_query, (id_corrida,))
        connection.commit()
        print(f"Corrida de ID {id_corrida} deletada com sucesso.")

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Corrida"
        cursor.execute(query)
        return cursor.fetchall()
