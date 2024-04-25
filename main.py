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
    print(f"\n----- {opcao} MENU DE OPERAÇÕES -----\n\n"
    "(1) Incluir.\n"
    "(2) Listar.\n"
    "(3) Atualizar.\n"
    "(4) Excluir.\n"
    "(9) Voltar ao menu principal.\n")
    
    return int(input('Digite a operação que deseja fazer: '))

def incluir_estudantes(arquivo):
    print("\n===== INCLUSÃO =====\n")
    while True:
        codigo = int(input("Digite o código do estudante: "))
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")
        novo_estudante = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
        
        if input("Deseja cadastrar um novo aluno? (s/n) ") == "n":
            print("Inclusão concluída.")
            break
        
    lista = ler_arquivo(arquivo)
    lista.append(novo_estudante)
    salvar_arquivo(lista, arquivo)

def listar_estudantes(arquivo):
    lista = ler_arquivo(arquivo)
    print("\n===== LISTAGEM =====\n")
    if len(lista) == 0:
        print("Nenhum estudante listado ainda.")
    else:
        for item in lista:
            print(f"-- Código: {item['Codigo']}, Nome: {item['Nome']}, CPF: {item['CPF']}")
        print("\nListagem concluída.")

def atualizar_estudantes(codigo, arquivo):
    lista = ler_arquivo(arquivo)
    print("\n===== ATUALIZAR =====\n")
    item_modificar = None
    
    for item in lista:
        if item["Codigo"] == codigo:
            item_modificar = item
            break
    if item_modificar == None:
        print("Nenhum estudante possui o código informado")
    else:
        item_modificar["Codigo"] = int(input("Digite o novo código: "))
        item_modificar["Nome"] = input("Digite o novo nome: ")
        item_modificar["CPF"] = input("Digite o novo CPF: ")
        salvar_arquivo(lista, arquivo)
        return

def excluir_estudantes(codigo, arquivo):
    lista = ler_arquivo(arquivo)
    print("\n===== EXCLUIR =====\n")
    item_excluido = None
    
    for dicionario in lista:
        if codigo == dicionario["Codigo"]:
            item_excluido = dicionario
            break
        
    if item_excluido is None:
        print("Nenhum estudante possui o código informado")
    else:
        lista.remove(item_excluido)
        salvar_arquivo(lista, arquivo)
        print("Estudante removido")
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
            return 'estudantes'
        case 2: 
            return 'professores'
        case 3: 
            return 'disciplinas'
        case 4:
            return 'turmas'
        case 5: 
            return 'matrículas'

def processar_menu_secundario(opcao_secundaria, arquivo):
    if opcao_secundaria == 1:
        incluir_estudantes(arquivo)
    elif opcao_secundaria == 2: 
        listar_estudantes(arquivo)
    elif opcao_secundaria == 3:
        try:
            codigo = int(input("Qual o código do estudante que você deseja atualizar? "))
        except:
            print('Apenas números são permitidos. Digite novamente.')
            return
        atualizar_estudantes(codigo, arquivo)
    elif opcao_secundaria == 4: 
        try:
            codigo = int(input("Qual o código do estudante que você deseja excluir? "))
        except:
            print('Apenas números são permitidos. Digite novamente.')
            return
        excluir_estudantes(codigo, arquivo)
    elif opcao_secundaria == 9: 
        print("Voltando para o menu principal")
        return False
    return True


arquivo_estudante = 'estudantes.json'
arquivo_professores = 'professores.json'

while True:
    try:
        opcao = menu_principal()
    except:
        print('Apenas números são permitidos. Digite novamente.')
        continue
    
    if opcao == 1:
        while True:
            escolha = opcao_selecionada(opcao)
            try:
                opcao_secundaria = menu_de_operacoes(escolha)
            except:
                print('Apenas números são permitidos. Digite novamente.')
                continue
            processar_menu_secundario(opcao_secundaria, arquivo_estudante )
    elif opcao == 2:
        while True:
            escolha = opcao_selecionada(opcao)
            try:
                opcao_secundaria = menu_de_operacoes(escolha)
            except:
                print('Apenas números são permitidos. Digite novamente.')
                continue
            processar_menu_secundario(opcao_secundaria, arquivo_professores)
    elif opcao >= 3 and opcao <= 5:
        print('EM DESENVOLVIMENTO')
    elif opcao == 6:
        break 
    else:
        print('Opção inválida, digite novamente')