import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        # Conexão ao banco de dados MySQL
        connection = mysql.connector.connect(
            host='localhost',         # Ou o IP do servidor MySQL
            database='c07_mk',        # Nome do banco de dados
            user='root',              # Usuário MySQL
            password='root' # Senha do MySQL
        )

        # Verificar se a conexão foi estabelecida
        if connection.is_connected():
            print("Conexão bem-sucedida ao MySQL")
            return connection
        else:
            print("Falha na conexão ao MySQL")
            return None

    except Error as e:
        # Imprimir qualquer erro de conexão
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexão fechada.")
