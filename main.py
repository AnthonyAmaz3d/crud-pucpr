"""
    Anthony Maia Dolberth
    Superior de Tecnologia em Análise e Desenvolvimento de Sistemas
"""

estudantes = []

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

def incluir_estudantes(estudantes):
    print("\n===== INCLUSÃO =====\n")
    while True:
        codigo = int(input("Digite o código do estudante: "))
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")
        novo_estudante = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
        estudantes.append(novo_estudante)
        if input("Deseja cadastrar um novo aluno? (s/n) ") == "n":
            print("Inclusão concluída.")
            break

def listagem_estudantes(estudantes):
    print("\n===== LISTAGEM =====\n")
    if len(estudantes) == 0:
        print("Nenhum estudante listado ainda.")
    else:
        for estudante in estudantes:
            print(f"-- Código: {estudante['Codigo']}, Nome: {estudante['Nome']}, CPF: {estudante['CPF']}")
        print("\nListagem concluída.")

def atualizacao_estudantes(estudantes):
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

def exclusao_estudantes(estudantes):
    print("\n===== EXCLUIR =====\n")
    codigo_estudante_excluido = int(input("Qual o código do estudante que você deseja excluir? "))
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

while True:
    main = menu_principal()
    if main == 'sair':
        print(f'Você escolheu a opção {main}, finalizando CRUD')
        break
    else:
        while True:
            operacao = menu_de_operacoes(main)
            if operacao == 1:
                incluir_estudantes(estudantes)
            elif operacao == 2: 
                listagem_estudantes(estudantes)
            elif operacao == 3:
                atualizacao_estudantes(estudantes)
            elif operacao == 4:
                exclusao_estudantes(estudantes)
            elif operacao == 9:
                break
            else:
                print('Opção inválida, tente novamente')