"""
    Anthony Maia Dolberth
    Superior de Tecnologia em Análise e Desenvolvimento de Sistemas
"""
import json

arquivo_estudante = "estudantes.json"

def menu_principal():
    print("----- MENU PRINCIPAL -----\n\n"
    "(1) Gerenciar estudantes.\n"
    "(2) Gerenciar professores.\n"
    "(3) Gerenciar disciplinas.\n"
    "(4) Gerenciar turmas.\n"
    "(5) Gerenciar matrículas.\n"
    "(9) Sair.\n")
    
    opcao = int(input('Digite a operação que deseja fazer: '))

    if opcao == 1:
        return 'estudantes'
    elif opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        print('EM DESENVOLVIMENTO')
        return menu_principal()
    elif opcao == 9:
        return 'sair'
    else:
        print('Opção inválida, tente novamente')
        return menu_principal()

def menu_de_operacoes(opcao):
    opcao = opcao.upper()
    print(f"\n----- [{opcao}] - MENU DE OPERAÇÕES -----\n\n"
    "(1) Incluir.\n"
    "(2) Listar.\n"
    "(3) Atualizar.\n"
    "(4) Excluir.\n"
    "(9) Voltar ao menu principal.\n")
    
    opcao_secundaria = int(input('Digite a operação que deseja fazer: '))
    return opcao_secundaria

def incluir_estudantes(nome_arquivo):
    print("\n===== INCLUSÃO =====\n")
    while True:
        codigo = int(input("Digite o código do estudante: "))
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")
        novo_estudante = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
        
        if input("Deseja cadastrar um novo aluno? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    estudantes = ler_arquivo(nome_arquivo)
    estudantes.append(novo_estudante)
    salvar_arquivos(estudantes, nome_arquivo)

def listar_estudantes(nome_arquivo):
    estudantes = ler_arquivo(nome_arquivo)
    print("\n===== LISTAGEM =====\n")
    if len(estudantes) == 0:
        print("Nenhum estudante listado ainda.")
    else:
        for estudante in estudantes:
            print(f"-- Código: {estudante['Codigo']}, Nome: {estudante['Nome']}, CPF: {estudante['CPF']}")
        print("\nListagem concluída.")

def atualizar_estudantes(nome_arquivo):
    estudantes = ler_arquivo(nome_arquivo)
    print("\n===== ATUALIZAR =====\n")
    codigo_estudante_editar = int(input("Qual o código do estudante que você deseja editar? "))
    estudante_modificar = None
    
    for dicionario in estudantes:
        if dicionario["Codigo"] == codigo_estudante_editar:
            estudante_modificar = dicionario
            break
    if estudante_modificar == None:
        print("Nenhum estudante possui o código informado")
    else:
        estudante_modificar["Codigo"] = int(input("Digite o novo código: "))
        estudante_modificar["Nome"] = input("Digite o novo nome: ")
        estudante_modificar["CPF"] = input("Digite o novo CPF: ")
        salvar_arquivos(estudantes, "estudantes.json")
        return

def excluir_estudantes(nome_arquivo):
    estudantes = ler_arquivo(nome_arquivo)
    print("\n===== EXCLUIR =====\n")
    try:
        codigo_estudante_excluido = int(input("Qual o código do estudante que você deseja excluir? "))
    except:
        print
    estudante_excluido = None
    
    for dicionario in estudantes:
        if codigo_estudante_excluido == dicionario["Codigo"]:
            estudante_excluido = dicionario
            break
        
    if estudante_excluido is None:
        print("Nenhum estudante possui o código informado")
    else:
        estudantes.remove(estudante_excluido)
        print("Estudante removido")
        salvar_arquivos(estudantes, "estudantes.json")
        return

def salvar_arquivos(lista, nome_arquivo):
    with open (nome_arquivo, 'w') as f:
        json.dump(lista, f)

def ler_arquivo(nome_arquivo):
    with open (nome_arquivo, 'r') as f:
        lista = json.load(f)
    
    return lista

while True:
    main = menu_principal()
    if main == 'sair':
        print(f'Você escolheu a opção {main}, finalizando CRUD')
        break
    else:
        while True:
            operacao = menu_de_operacoes(main)
            if operacao == 1:
                incluir_estudantes(arquivo_estudante)
            elif operacao == 2: 
                listar_estudantes(arquivo_estudante)
            elif operacao == 3:
                atualizar_estudantes(arquivo_estudante)
            elif operacao == 4:
                excluir_estudantes(arquivo_estudante)
            elif operacao == 9:
                break
            else:
                print('Opção inválida, tente novamente')