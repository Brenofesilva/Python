import json

from entrada import *

def adicionar_aluno(id):
    nome = input("Digite o nome do aluno: ")
    idade = ler_inteiro("Digite a idade do aluno: ", True)
    peso = ler_real("Digite o peso do aluno: ", True)
    altura = ler_real("Digite a altura do aluno: ", True)
    
#dicionário aluno
    adicionar_aluno = {
        "id": id,
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "imc": round((peso / altura), 2)
    }
    
    return  adicionar_aluno
    
def mostrar_alunos(alunos):
    alunos_salvos = open('alunos.json', 'r')
    total_alunos = json.load(alunos_salvos) + alunos
    for aluno in total_alunos:
        print(aluno)


def buscar_aluno_id(alunos_list):
        alunos_salvos = open('alunos.json', 'r')
        alunos = json.load(alunos_salvos) + alunos_list
        busca_id = ler_inteiro("Digite o id do aluno que deseja buscar: ", pos=True)  # função next procura o primeiro id na lista # função pos = True verifica se o número é positivo ou 0, só é aceito número positivo
        aluno_encontrado = next(
            (aluno for aluno in alunos if aluno["id"] == busca_id), None
        )  # aluno encontrado
        if aluno_encontrado:  # se encontrado, exibe os dados na tela
            print(f"Aluno encontrado: Nome: {aluno_encontrado['nome']}, idade: {aluno_encontrado['idade']}, peso: {aluno_encontrado['peso']}, altura: {aluno_encontrado['altura']}, imc: {aluno_encontrado['imc']}")
        else:
            print("Aluno não encontrado")

def buscar_aluno_imc(alunos_list):
    alunos_salvos = open('alunos.json', 'r')
    alunos = json.load(alunos_salvos) + alunos_list
    imc = ler_real("Valor do IMC: ", pos=True)
    aluno_encontrado = next((aluno for aluno in alunos if aluno["imc"] == imc), None)  # aluno encontrado
    if aluno_encontrado:  # se encontrado, exibe os dados na tela
        print(f"Aluno encontrado: Nome: {aluno_encontrado['nome']}, idade: {aluno_encontrado['idade']}, peso: {aluno_encontrado['peso']}, altura: {aluno_encontrado['altura']}, imc: {aluno_encontrado['imc']}")
    else:
        print("Aluno não encontrado")  
  
def salvar_alunos(alunos_list):
    alunos_salvos = open('alunos.json', 'r')
    alunos = json.load(alunos_salvos) + alunos_list
    with open('alunos.json', 'w') as file:
        file.write(json.dumps(alunos))
    print("DADOS SALVOS")

