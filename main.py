from aluno import *
from entrada import *
from navegabilidade import *
import json

# variáveis de controle dos dados na memória

def encontrar_proximo_id():
    with open('alunos.json') as file:
        lastId = len(json.load(file))
        if lastId >= 1: 
            return lastId + 1
        else: return 1


id = encontrar_proximo_id()
alunos = []

programa_ativo = True  # O programa continua ativo até que seja definido o False, que é o encerramento do programa

while programa_ativo:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    # navegabilidade
    if opc == 1:  # cadastra aluno
        novo_aluno = adicionar_aluno(
            id
        )  # chama a função que coleta os dados e retorna um dicionário preenchido
        alunos.append(novo_aluno)  # adiciona o novo aluno a lista de alunos
        id += 1  # incrementa o id para o próximo aluno
        print("Aluno adicionado com sucesso!")

        # função lê os dados de aluno e retorna um dicionário
        # dicionário é adicionado na lista de alunos

    elif opc == 2:
        mostrar_alunos(alunos)
        # função imprime todos os alunos em tela

    elif opc == 3:  # Busca o aluno por id
        buscar_aluno_id(alunos)

        # busca um aluno por id e apresenta seus dados se existir

    elif opc == 4:  # filtra alunos pelo IMC
        buscar_aluno_imc(alunos)


    elif (
        opc == 5
    ):  # salva todos os dados inseridos, e pergunta pro usuário se ele deseja sair ou continuar
        salvar_alunos(alunos)
        break


    limpar_tela()
