class KartDAO:

    @staticmethod
    def insert(connection, kart):
        cursor = connection.cursor()
        query = """
            INSERT INTO Kart (Modelo, velocidade_max, Jogador_idJogador) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (kart['Modelo'], kart['velocidade_max'], kart['Jogador_idJogador']))
        connection.commit()
        print(f"Cart {kart['Modelo']} inserido com sucesso.")

    @staticmethod
    def update(connection, id_kart, kart):
        cursor = connection.cursor()
        query = "UPDATE Kart SET "
        values = []

        if 'Modelo' in kart:
            query += "Modelo = %s, "
            values.append(kart['Modelo'])

        if 'velocidade_max' in kart:
            query += "velocidade_max = %s, "
            values.append(kart['velocidade_max'])

        if 'Jogador_idJogador' in kart:
            query += "Jogador_idJogador = %s, "
            values.append(kart['Jogador_idJogador'])

        query = query.rstrip(', ') + " WHERE id_Kart = %s"
        values.append(id_kart)

        cursor.execute(query, tuple(values))
        connection.commit()
        print(f"Cart de ID {id_kart} atualizado com sucesso.")
