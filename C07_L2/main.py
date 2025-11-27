from db.jogador_dao import JogadorDAO
from db.personagem_dao import PersonagemDAO
from db.kart_dao import KartDAO
from db.pista_dao import PistaDAO
from db.corrida_dao import CorridaDAO
from db.conquista_dao import ConquistaDAO
from db.joins import select_players_with_characters, select_karts_with_players, select_races_with_tracks, select_players_with_conquests, select_races_with_players, select_karts_with_conquests
from db.connection_dao import get_connection, close_connection

# Função para exibir o menu
def show_menu():
    print("\nEscolha uma operação:")
    print("1. Inserir dado")
    print("2. Atualizar dado")
    print("3. Deletar dado")
    print("4. Consultar dados com JOIN")
    print("5. Sair")

# Função para exibir o menu de JOINs
def show_join_menu():
    print("\nEscolha uma consulta JOIN:")
    print("1. Jogadores com Personagens")
    print("2. Karts com Jogadores")
    print("3. Corridas com Pistas")
    print("4. Jogadores com Conquistas")
    print("5. Corridas com Jogadores")
    print("6. Karts com Conquistas")
    print("7. Voltar")

def main():
    # Estabelecer a conexão com o banco de dados
    connection = get_connection()

    if connection:
        print("Iniciando o menu interativo...")

        while True:
            show_menu()
            choice = input("Escolha uma opção: ")

            if choice == "1":
                # Inserir dado - agora vai pedir todos os dados necessários para as tabelas
                print("\nEscolha a tabela para inserir:")
                print("1. Personagem")
                print("2. Jogador")
                print("3. Kart")
                print("4. Pista")
                print("5. Corrida")
                print("6. Conquista")
                tabela = input("Escolha a tabela: ")

                if tabela == "1":  # Inserir na tabela Personagem
                    nome = input("Digite o nome do personagem: ")
                    habilidade_especial = input("Digite a habilidade especial do personagem: ")
                    PersonagemDAO.insert(connection, {'Nome': nome, 'habilidade_especial': habilidade_especial})

                elif tabela == "2":  # Inserir na tabela Jogador
                    nick_name = input("Digite o nick do jogador: ")
                    personagem_id = input("Digite o id do personagem: ")
                    idade = input("Digite a idade do jogador: ")
                    if personagem_id.isdigit() and idade.isdigit():
                        JogadorDAO.insert(connection, {'nick_name': nick_name, 'Personagem_idPersonagem': int(personagem_id), 'idade': int(idade)})

                elif tabela == "3":  # Inserir na tabela Kart
                    modelo = input("Digite o modelo do kart: ")
                    velocidade_max = input("Digite a velocidade máxima do kart: ")
                    jogador_id = input("Digite o id do jogador: ")
                    if velocidade_max.isdigit() and jogador_id.isdigit():
                        KartDAO.insert(connection, {'Modelo': modelo, 'velocidade_max': float(velocidade_max), 'Jogador_idJogador': int(jogador_id)})

                elif tabela == "4":  # Inserir na tabela Pista
                    nome = input("Digite o nome da pista: ")
                    dificuldade = input("Digite a dificuldade da pista: ")
                    PistaDAO.insert(connection, {'nome': nome, 'dificuldade': dificuldade})

                elif tabela == "5":  # Inserir na tabela Corrida
                    data = input("Digite a data da corrida: ")
                    tempo_total = input("Digite o tempo total da corrida: ")
                    pista_id = input("Digite o id da pista: ")
                    if pista_id.isdigit():
                        CorridaDAO.insert(connection, {'data': data, 'tempo_total': tempo_total, 'Corrida_id_pista': int(pista_id)})

                elif tabela == "6":  # Inserir na tabela Conquista
                    descricao = input("Digite a descrição da conquista: ")
                    nome_conquista = input("Digite o nome da conquista: ")
                    ConquistaDAO.insert(connection, {'descricao': descricao, 'nome': nome_conquista})

            elif choice == "2":
                # Atualizar dado - agora o usuário pode escolher qualquer tabela e campo para atualizar
                print("\nEscolha a tabela para atualizar:")
                print("1. Personagem")
                print("2. Jogador")
                print("3. Kart")
                print("4. Pista")
                print("5. Corrida")
                print("6. Conquista")
                tabela = input("Escolha a tabela: ")

                if tabela == "1":  # Atualizar na tabela Personagem
                    id_personagem = input("Digite o id do personagem para atualizar: ")
                    novo_nome = input("Digite o novo nome do personagem: ")
                    nova_habilidade = input("Digite a nova habilidade especial do personagem: ")
                    if id_personagem.isdigit():
                        PersonagemDAO.update(connection, int(id_personagem), {'Nome': novo_nome, 'habilidade_especial': nova_habilidade})

                elif tabela == "2":  # Atualizar na tabela Jogador
                    id_jogador = input("Digite o id do jogador para atualizar: ")
                    novo_nick_name = input("Digite o novo nick do jogador: ")
                    nova_idade = input("Digite a nova idade do jogador: ")
                    if id_jogador.isdigit() and nova_idade.isdigit():
                        JogadorDAO.update(connection, int(id_jogador), {'nick_name': novo_nick_name, 'idade': int(nova_idade)})

                elif tabela == "3":  # Atualizar na tabela Kart
                    id_kart = input("Digite o id do kart para atualizar: ")
                    novo_modelo = input("Digite o novo modelo do kart: ")
                    nova_velocidade_max = input("Digite a nova velocidade máxima do kart: ")
                    if id_kart.isdigit() and nova_velocidade_max.isdigit():
                        KartDAO.update(connection, int(id_kart), {'Modelo': novo_modelo, 'velocidade_max': float(nova_velocidade_max)})

                elif tabela == "4":  # Atualizar na tabela Pista
                    id_pista = input("Digite o id da pista para atualizar: ")
                    novo_nome = input("Digite o novo nome da pista: ")
                    nova_dificuldade = input("Digite a nova dificuldade da pista: ")
                    if id_pista.isdigit():
                        PistaDAO.update(connection, int(id_pista), {'nome': novo_nome, 'dificuldade': nova_dificuldade})

                elif tabela == "5":  # Atualizar na tabela Corrida
                    id_corrida = input("Digite o id da corrida para atualizar: ")
                    nova_data = input("Digite a nova data da corrida: ")
                    novo_tempo_total = input("Digite o novo tempo total da corrida: ")
                    if id_corrida.isdigit():
                        CorridaDAO.update(connection, int(id_corrida), {'data': nova_data, 'tempo_total': novo_tempo_total})

                elif tabela == "6":  # Atualizar na tabela Conquista
                    id_conquista = input("Digite o id da conquista para atualizar: ")
                    nova_descricao = input("Digite a nova descrição da conquista: ")
                    novo_nome_conquista = input("Digite o novo nome da conquista: ")
                    if id_conquista.isdigit():
                        ConquistaDAO.update(connection, int(id_conquista), {'descricao': nova_descricao, 'nome': novo_nome_conquista})

            elif choice == "3":
                # Deletar dado
                id_jogador = input("Digite o id do jogador para excluir: ")
                if id_jogador.isdigit():
                    JogadorDAO.delete(connection, int(id_jogador))
                    print(f"Jogador de ID {id_jogador} deletado com sucesso.")
                else:
                    print("ID inválido. Por favor, insira um número válido.")

            elif choice == "4":
                # Consultar dados com JOIN
                show_join_menu()
                join_choice = input("Escolha a consulta JOIN: ")

                if join_choice == "1":
                    # Jogadores com Personagens
                    players = select_players_with_characters(connection)
                    for player in players:
                        print(player)

                elif join_choice == "2":
                    # Karts com Jogadores
                    karts = select_karts_with_players(connection)
                    for kart in karts:
                        print(kart)

                elif join_choice == "3":
                    # Corridas com Pistas
                    races = select_races_with_tracks(connection)
                    for race in races:
                        print(race)

                elif join_choice == "4":
                    # Jogadores com Conquistas
                    players_conquests = select_players_with_conquests(connection)
                    for player_conquest in players_conquests:
                        print(player_conquest)

                elif join_choice == "5":
                    # Corridas com Jogadores
                    races_players = select_races_with_players(connection)
                    for race_player in races_players:
                        print(race_player)

                elif join_choice == "6":
                    # Karts com Conquistas
                    karts_conquests = select_karts_with_conquests(connection)
                    for kart_conquest in karts_conquests:
                        print(kart_conquest)

                elif join_choice == "7":
                    # Voltar
                    continue

            elif choice == "5":
                # Sair
                print("Saindo...")
                break

        close_connection(connection)

    else:
        print("Não foi possível conectar ao banco de dados.")

if __name__ == "__main__":
    main()
