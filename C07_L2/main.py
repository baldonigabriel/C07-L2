from db.joins import select_players_with_characters
from db.jogador_dao import JogadorDAO
from db.connection_dao import get_connection, close_connection

# Função para exibir o menu
def show_menu():
    print("\nEscolha uma operação:")
    print("1. Inserir dado")
    print("2. Atualizar dado")
    print("3. Deletar dado")
    print("4. Consultar dados com JOIN")
    print("5. Sair")

def main():
    # Estabelecer a conexão com o banco de dados
    connection = get_connection()

    if connection:
        print("Iniciando o menu interativo...")

        while True:
            show_menu()
            choice = input("Escolha uma opção: ")

            if choice == "1":
                # Inserir dado
                nick_name = input("Digite o nick do jogador: ")
                personagem_id = input("Digite o id do personagem: ")

                # Verifica se o valor de idPersonagem é numérico
                if personagem_id.isdigit():
                    jogador = {'nick_name': nick_name, 'Personagem_idPersonagem': int(personagem_id)}
                    JogadorDAO.insert(connection, jogador)
                    print(f"Jogador {nick_name} inserido com sucesso.")
                else:
                    print("ID do personagem inválido. Por favor, insira um número.")

            elif choice == "2":
                # Atualizar dado
                id_jogador = input("Digite o id do jogador para atualizar: ")
                novo_nick_name = input("Digite o novo nick do jogador: ")

                if id_jogador.isdigit():
                    JogadorDAO.update(connection, int(id_jogador), {'nick_name': novo_nick_name})
                    print(f"Jogador de ID {id_jogador} atualizado para {novo_nick_name}.")
                else:
                    print("ID inválido. Por favor, insira um número válido.")

            elif choice == "3":
                # Deletar dado
                id_jogador = input("Digite o id do jogador para excluir: ")

                if id_jogador.isdigit():
                    JogadorDAO.delete(connection, int(id_jogador))  # Chamada para deletar jogador
                    print(f"Jogador de ID {id_jogador} deletado com sucesso.")
                else:
                    print("ID inválido. Por favor, insira um número válido.")

            elif choice == "4":
                # Consultar dados com JOIN
                players = select_players_with_characters(connection)
                for player in players:
                    print(player)

            elif choice == "5":
                # Sair
                print("Saindo...")
                break

        close_connection(connection)

    else:
        print("Não foi possível conectar ao banco de dados.")

if __name__ == "__main__":
    main()
