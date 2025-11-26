class PersonagemDAO:

    @staticmethod
    def insert(connection, personagem):
        cursor = connection.cursor()
        query = "INSERT INTO Personagem (Nome, habilidade_especial) VALUES (%s, %s)"
        cursor.execute(query, (personagem['Nome'], personagem['habilidade_especial']))
        connection.commit()

    @staticmethod
    def update(connection, id_personagem, personagem):
        cursor = connection.cursor()
        query = "UPDATE Personagem SET Nome = %s, habilidade_especial = %s WHERE idPersonagem = %s"
        cursor.execute(query, (personagem['Nome'], personagem['habilidade_especial'], id_personagem))
        connection.commit()

    @staticmethod
    def delete(connection, id_personagem):
        cursor = connection.cursor()
        query = "DELETE FROM Personagem WHERE idPersonagem = %s"
        cursor.execute(query, (id_personagem,))
        connection.commit()

    @staticmethod
    def select(connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Personagem"
        cursor.execute(query)
        return cursor.fetchall()
