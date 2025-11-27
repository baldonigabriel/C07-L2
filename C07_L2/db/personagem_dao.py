class PersonagemDAO:

    @staticmethod
    def insert(connection, personagem):
        cursor = connection.cursor()
        query = """
            INSERT INTO Personagem (Nome, habilidade_especial) 
            VALUES (%s, %s)
        """
        cursor.execute(query, (personagem['Nome'], personagem['habilidade_especial']))
        connection.commit()
        print(f"Personagem {personagem['Nome']} inserido com sucesso.")

    @staticmethod
    def update(connection, id_personagem, personagem):
        cursor = connection.cursor()
        query = "UPDATE Personagem SET "
        values = []

        if 'Nome' in personagem:
            query += "Nome = %s, "
            values.append(personagem['Nome'])

        if 'habilidade_especial' in personagem:
            query += "habilidade_especial = %s, "
            values.append(personagem['habilidade_especial'])

        query = query.rstrip(', ') + " WHERE idPersonagem = %s"
        values.append(id_personagem)

        cursor.execute(query, tuple(values))
        connection.commit()
        print(f"Personagem de ID {id_personagem} atualizado com sucesso.")
