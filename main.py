"""
    Anthony Maia Dolberth
    Superior de Tecnologia em Análise e Desenvolvimento de Sistemas
"""
import json

def menu_principal():
    print("----- MENU PRINCIPAL -----\n\n"
    "(1) Gerenciar estudantes.\n"
    "(2) Gerenciar professores.\n"
    "(3) Gerenciar disciplinas.\n"
    "(4) Gerenciar turmas.\n"
    "(5) Gerenciar matrículas.\n"
    "(9) Sair.\n")
    
    return int(input('Digite a operação que deseja fazer: '))

def menu_de_operacoes(opcao):
    opcao = opcao.upper()
    print(f"\n----- [{opcao}] MENU DE OPERAÇÕES -----\n\n"
    "(1) Incluir.\n"
    "(2) Listar.\n"
    "(3) Atualizar.\n"
    "(4) Excluir.\n"
    "(9) Voltar ao menu principal.\n")
    
    return int(input('Digite a operação que deseja fazer: '))

def incluir_estudantes_ou_professores(arquivo, opcao):
    opcao_selecionada(opcao)
    print(f"\n===== INCLUSÃO DE {opcao.upper()} =====\n")
    while True:
        codigo = int(input(f"Digite o código do {opcao}: "))
        nome = input(f"Digite o nome do {opcao}: ")
        cpf = input(f"Digite o CPF do {opcao}: ")
        novo_cadastro = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
        
        if input("Deseja cadastrar uma nova pessoa? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    lista = ler_arquivo(arquivo)
    lista.append(novo_cadastro)
    salvar_arquivo(lista, arquivo)

def incluir_matricula_ou_turma(arquivo, opcao):
    opcao_selecionada(opcao)
    print(f"\n===== INCLUSÃO DE {opcao.upper()} =====\n")
    while True:
        codigo = int(input(f"Digite o código do {opcao}: "))
        numero = input(f"Digite o número da {opcao}: ")
        novo_cadastro = {'Codigo': codigo, 'Numero': numero}
        
        if input("Deseja realizar outro cadastro? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    lista = ler_arquivo(arquivo)
    lista.append(novo_cadastro)
    salvar_arquivo(lista, arquivo)

def incluir_disciplina(arquivo, opcao):
    opcao_selecionada(opcao)
    print(f"\n===== INCLUSÃO DE {opcao.upper()} =====\n")
    while True:
        codigo = int(input(f"Digite o código do {opcao}: "))
        nome = input(f"Digite o nome da {opcao}: ")
        novo_cadastro = {'Codigo': codigo, 'Nome': nome}
        
        if input("Deseja realizar outro cadastro? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    lista = ler_arquivo(arquivo)
    lista.append(novo_cadastro)
    salvar_arquivo(lista, arquivo)

def listar_estudantes_ou_professores(arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== LISTAGEM DE {opcao.upper()} =====\n")
    if len(lista) == 0:
        print(f"Nenhum/a {opcao} listado/a ainda.")
    else:
        for item in lista:
            print(f"-- Código: {item['Codigo']}, Nome: {item['Nome']}, CPF: {item['CPF']}")
        print("\nListagem concluída.")

def listar_matricula_ou_turma(arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== LISTAGEM DE {opcao.upper()} =====\n")
    if len(lista) == 0:
        print(f"Nenhum/a {opcao} listado/a ainda.")
    else:
        for item in lista:
            print(f"-- Código: {item['Codigo']}, Numero: {item['Numero']}")
        print("\nListagem concluída.")

def listar_discplina(arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== LISTAGEM DE {opcao.upper()} =====\n")
    if len(lista) == 0:
        print(f"Nenhum/a {opcao} listado/a ainda.")
    else:
        for item in lista:
            print(f"-- Código: {item['Codigo']}, Nome: {item['Nome']}")
        print("\nListagem concluída.")

def atualizar_estudantes_ou_professores(codigo, arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== ATUALIZAR {opcao.upper()} =====\n")
    item_modificar = None
    
    for item in lista:
        if item["Codigo"] == codigo:
            item_modificar = item
            break
    if item_modificar == None:
        print("Nenhum cadastro possui o código informado")
    else:
        item_modificar["Codigo"] = int(input("Digite o novo código: "))
        item_modificar["Nome"] = input("Digite o novo nome: ")
        item_modificar["CPF"] = input("Digite o novo CPF: ")
        salvar_arquivo(lista, arquivo)
        return

def atualizar_matricula_ou_turma(codigo, arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== ATUALIZAR {opcao.upper()} =====\n")
    item_modificar = None
    
    for item in lista:
        if item["Codigo"] == codigo:
            item_modificar = item
            break
    if item_modificar == None:
        print("Nenhum cadastro possui o código informado")
    else:
        item_modificar["Codigo"] = int(input("Digite o novo código: "))
        item_modificar["Numero"] = input("Digite o novo número: ")
        salvar_arquivo(lista, arquivo)
        return

def atualizar_disciplina(codigo, arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== ATUALIZAR {opcao.upper()} =====\n")
    item_modificar = None
    
    for item in lista:
        if item["Codigo"] == codigo:
            item_modificar = item
            break
    if item_modificar == None:
        print("Nenhum cadastro possui o código informado")
    else:
        item_modificar["Codigo"] = int(input("Digite o novo código: "))
        item_modificar["Nome"] = input("Digite o novo nome: ")
        salvar_arquivo(lista, arquivo)
        return

def excluir_cadastro(codigo, arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== EXCLUIR {opcao.upper()} =====\n")
    item_excluido = None
    
    for dicionario in lista:
        if codigo == dicionario["Codigo"]:
            item_excluido = dicionario
            break
        
    if item_excluido is None:
        print(f"Nenhum {opcao} possui o código informado")
    else:
        lista.remove(item_excluido)
        salvar_arquivo(lista, arquivo)
        print(f"{opcao} removido")
        return

def salvar_arquivo(lista, arquivo):
    with open (arquivo, 'w') as f:
        json.dump(lista, f)

def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            lista = json.load(f)
        return lista
    except:
        return []

def opcao_selecionada(opcao):
    match opcao:
        case 1:
            return 'estudante'
        case 2: 
            return 'professor'
        case 3: 
            return 'disciplina'
        case 4:
            return 'turma'
        case 5: 
            return 'matrícula'

def processar_menu_secundario(opcao_secundaria, arquivo, opcao, opcao2):
    if opcao_secundaria == 1:
        if opcao2 == 1 or opcao2 == 2:
            incluir_estudantes_ou_professores(arquivo, opcao)
        elif opcao2 == 4 or opcao2 == 5:
            incluir_matricula_ou_turma(arquivo, opcao)
        else:
            incluir_disciplina(arquivo, opcao)

    elif opcao_secundaria == 2: 
        if opcao2 == 1 or opcao2 == 2:
            listar_estudantes_ou_professores(arquivo, opcao)
        elif opcao2 == 4 or opcao2 == 5:
            listar_matricula_ou_turma(arquivo, opcao)
        else:
            listar_discplina(arquivo, opcao)

    elif opcao_secundaria == 3:
        try:
            codigo = int(input(f"Qual o código do {opcao} que você deseja atualizar? "))
        except:
            print('Apenas números são permitidos. Digite novamente.')
            return
        if opcao2 == 1 or opcao2 == 2:
            atualizar_estudantes_ou_professores(codigo, arquivo, opcao)
        elif opcao2 == 4 or opcao2 == 5:
            atualizar_matricula_ou_turma(codigo, arquivo, opcao)
        else: 
            atualizar_disciplina(codigo, arquivo, opcao)

    elif opcao_secundaria == 4: 
        try:
            codigo = int(input(f"Qual o código do {opcao} que você deseja excluir? "))
        except:
            print('Apenas números são permitidos. Digite novamente.')
            return
        excluir_cadastro(codigo, arquivo, opcao)

    elif opcao_secundaria == 9: 
        print("Voltando para o menu principal")
        return False
    return True


arquivo_estudante = 'estudantes.json'
arquivo_professor = 'professores.json'
arquivo_disciplina = 'disciplinas.json'
arquivo_turma = 'turmas.json'
arquivo_matricula = 'matriculas.json'

while True:
    try:
        opcao = menu_principal()
    except:
        print('Apenas números são permitidos. Digite novamente.')
        continue
    
    if opcao == 1:
        segunda_opcao = 1
        while True:
            escolha = opcao_selecionada(opcao)
            try:
                opcao_secundaria = menu_de_operacoes(escolha)
            except:
                print('Apenas números são permitidos. Digite novamente.')
                continue
            if not processar_menu_secundario(opcao_secundaria, arquivo_estudante, escolha, segunda_opcao):
                break

    elif opcao == 2:
        segunda_opcao = 2
        while True:
            escolha = opcao_selecionada(opcao)
            try:
                opcao_secundaria = menu_de_operacoes(escolha)
            except:
                print('Apenas números são permitidos. Digite novamente.')
                continue
            if not processar_menu_secundario(opcao_secundaria, arquivo_professor, escolha, segunda_opcao):
                break
    
    elif opcao == 3:
        segunda_opcao = 3
        while True:
            escolha = opcao_selecionada(opcao)
            try:
                opcao_secundaria = menu_de_operacoes(escolha)
            except:
                print('Apenas números são permitidos. Digite novamente.')
                continue
            if not processar_menu_secundario(opcao_secundaria, arquivo_disciplina, escolha, segunda_opcao):
                break
    
    elif opcao == 4:
        segunda_opcao = 4
        while True:
            escolha = opcao_selecionada(opcao)
            try:
                opcao_secundaria = menu_de_operacoes(escolha)
            except:
                print('Apenas números são permitidos. Digite novamente.')
                continue
            if not processar_menu_secundario(opcao_secundaria, arquivo_turma, escolha, segunda_opcao):
                break
    
    elif opcao == 5:
        segunda_opcao = 5
        while True:
            escolha = opcao_selecionada(opcao)
            try:
                opcao_secundaria = menu_de_operacoes(escolha)
            except:
                print('Apenas números são permitidos. Digite novamente.')
                continue
            if not processar_menu_secundario(opcao_secundaria, arquivo_matricula, escolha, segunda_opcao):
                break
    
    elif opcao == 9:
        print("Saindo do CRUD")
        break 
    else:
        print('Opção inválida, digite novamente')