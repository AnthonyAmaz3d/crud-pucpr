print("----- MENU PRINCIPAL -----\n\n"
    "(1) Gerenciar estudantes.\n"
    "(2) Gerenciar professores.\n"
    "(3) Gerenciar disciplinas.\n"
    "(4) Gerenciar turmas.\n"
    "(5) Gerenciar matrículas.\n"
    "(9) Sair.\n")
opcao = input("Informe a opção desejada: ")

if opcao == "1":
    print("\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n\n")
elif opcao == "2":
    print("\n***** [PROFESSORES] MENU DE OPERAÇÕES *****\n\n")
elif opcao == "3": 
    print("\n***** [DISCIPLINAS] MENU DE OPERAÇÕES *****\n\n")
elif opcao == "4": 
    print("\n***** [TURMAS] MENU DE OPERAÇÕES *****\n\n")
elif opcao == "5":
    print("\n***** [MATRICULAS] MENU DE OPERAÇÕES *****\n\n")
elif opcao =="9":
    print("\nFinalizando aplicação...\n")
    exit()
else: 
    print("Nenhuma opção correspondente, finalizando aplicação...")
    exit()

print("(1) Incluir.\n"
    "(2) Listar.\n"
    "(3) Atualizar.\n"
    "(4) Excluir.\n"
    "(9) Voltar ao menu principal.\n")

opcao = input("Informe a opção desejada: ")

if opcao == "1":
    print("\n===== INCLUINDO =====\n\n"
        "Inclusão concluida...")
elif opcao == "2":
    print("\n===== LISTANDO =====\n\n"
        "Listagem concluida...")
elif opcao == "3":
    print("\n===== ATUALIZANDO =====\n\n"
        "Atualização concluida...")
elif opcao == "4":
    print("\n===== EXCLUINDO =====\n\n"
        "Exclusão concluida...")
elif opcao == "9":
    print("\n===== VOLTANDO AO MENU PRINCIPAL =====\n\n")
else:
    print("Opção inválida, finalizando aplicação\n")
    exit()

print("\nProcesso finalizado\n")