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
    lista = ler_arquivo(arquivo)
    opcao_selecionada(opcao)
    print(f"\n===== INCLUSÃO DE {opcao.upper()} =====\n")
    while True:
        try:
            codigo = int(input(f"Digite o código do {opcao}: "))
        except:
            print("Apenas números são válidos.")
            continue
        for item in lista:
            if item['Codigo'] == codigo:
                print('Esse código ja existe, tente novamente')
                return incluir_estudantes_ou_professores(arquivo, opcao)
        nome = input(f"Digite o nome do {opcao}: ")
        cpf = input(f"Digite o CPF do {opcao}: ")
        novo_cadastro = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
        if input("Deseja cadastrar uma nova pessoa? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    lista.append(novo_cadastro)
    salvar_arquivo(lista, arquivo)

def incluir_turma(arquivo, opcao):
    lista = ler_arquivo(arquivo)
    opcao_selecionada(opcao)
    print(f"\n===== INCLUSÃO DE {opcao.upper()} =====\n")
    while True:
        try:
            codigo_turma = int(input(f"Digite o código da {opcao}: "))
            for item in lista:
                if item['Codigo'] == codigo_turma:
                    print('Esse código ja existe, tente novamente')
                    return incluir_turma(arquivo, opcao)
            codigo_professor = int(input(f"Digite o código do professor da {opcao}: "))
            codigo_disciplina = int(input(f"Digite o código da disciplina da {opcao}: "))
        except:
            print("Apenas números são válidos.")
            continue
        
        novo_cadastro = {'Codigo': codigo_turma, 'Codigo_professor': codigo_professor, 'Codigo_disciplina': codigo_disciplina}
        
        if input("Deseja realizar outro cadastro? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    lista.append(novo_cadastro)
    salvar_arquivo(lista, arquivo)

def incluir_matricula(arquivo, opcao):
    lista = ler_arquivo(arquivo)
    opcao_selecionada(opcao)
    print(f"\n===== INCLUSÃO DE {opcao.upper()} =====\n")
    while True:
        try:
            codigo_matricula = int(input(f"Digite o código do/a {opcao}: "))
            for item in lista:
                if item['Codigo'] == codigo_matricula:
                    print('Esse código ja existe, tente novamente')
                    return incluir_matricula(arquivo, opcao)
            codigo_estudante = int(input(f"Digite o código do estudante da {opcao}: "))
        except:
            print("Apenas números são válidos.")
            continue
        novo_cadastro = {'Codigo': codigo_matricula, 'Codigo_estudante': codigo_estudante}
        
        if input("Deseja realizar outro cadastro? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    lista.append(novo_cadastro)
    salvar_arquivo(lista, arquivo)

def incluir_disciplina(arquivo, opcao):
    opcao_selecionada(opcao)
    print(f"\n===== INCLUSÃO DE {opcao.upper()} =====\n")
    while True:
        try:
            codigo = int(input(f"Digite o código da {opcao}: "))
            for item in lista:
                if item['Codigo'] == codigo:
                    print('Esse código ja existe, tente novamente')
                    return incluir_turma(arquivo, opcao)
        except:
            print("Apenas números são válidos.")
            continue
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

def listar_matricula(arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== LISTAGEM DE {opcao.upper()} =====\n")
    if len(lista) == 0:
        print(f"Nenhum/a {opcao} listado/a ainda.")
    else:
        for item in lista:
            print(f"-- Código da matrícula: {item['Codigo']}, Código do estudante: {item['Codigo_estudante']}")
        print("\nListagem concluída.")

def listar_turma(arquivo, opcao):
    opcao_selecionada(opcao)
    lista = ler_arquivo(arquivo)
    print(f"\n===== LISTAGEM DE {opcao.upper()} =====\n")
    if len(lista) == 0:
        print(f"Nenhum/a {opcao} listado/a ainda.")
    else:
        for item in lista:
            print(f"-- Código da turma: {item['Codigo']}, Código do professor: {item['Codigo_professor']}, Código da disciplina: {item['Codigo_disciplina']}")
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

def atualizar_matricula(codigo, arquivo, opcao):
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
        item_modificar["Codigo"] = int(input("Digite o novo código da matrícula: "))
        item_modificar["Codigo_estudante"] = int(input("Digite o novo código do estudante: "))
        salvar_arquivo(lista, arquivo)
        return

def atualizar_turma(codigo, arquivo, opcao):
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
        item_modificar["Codigo"] = int(input("Digite o novo código da turma: "))
        item_modificar["Codigo_professor"] = int(input("Digite o novo código do professor: "))
        item_modificar["Codigo_disciplina"] = int(input("Digite o novo código da disciplina: "))
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
        elif opcao2 == 4:
            incluir_turma(arquivo, opcao)
        elif opcao2 == 5:
            incluir_matricula(arquivo, opcao)
        else:
            incluir_disciplina(arquivo, opcao)

    elif opcao_secundaria == 2: 
        if opcao2 == 1 or opcao2 == 2:
            listar_estudantes_ou_professores(arquivo, opcao)
        elif opcao2 == 4:
            listar_turma(arquivo, opcao)
        elif opcao2 == 5:
            listar_matricula(arquivo, opcao)
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
        elif opcao2 == 4:
            atualizar_turma(codigo, arquivo, opcao)
        elif opcao2 == 5:
            atualizar_matricula(codigo, arquivo, opcao)
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