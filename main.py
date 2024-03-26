while True:
    print("----- MENU PRINCIPAL -----\n\n"
    "(1) Gerenciar estudantes.\n"
    "(2) Gerenciar professores.\n"
    "(3) Gerenciar disciplinas.\n"
    "(4) Gerenciar turmas.\n"
    "(5) Gerenciar matrículas.\n"
    "(9) Sair.\n")
    
    opcao = input("Informe a opção desejada: ")
    
    if opcao == "9":
        print("\nFinalizando aplicação...\n")
        break
    else:
        while True:
            match opcao:
                case "1":
                    print("\n----- GERENCIAR ESTUDANTES -----\n")
                case "2":
                    print("\n----- GERENCIAR PROFESSORES -----\n")
                case "3":
                    print("\n----- GERENCIAR DISCIPLINAS -----\n")
                case "4":
                    print("\n----- GERENCIAR TURMAS -----\n")
                case "5":
                    print("\n----- GERENCIAR MATRÍCULAS -----\n")
                case _:
                    print("Nenhuma opção correspondente, digite novamente\n")

            print("(1) Incluir.\n"
                "(2) Listar.\n"
                "(3) Atualizar.\n"
                "(4) Excluir.\n"
                "(9) Voltar ao menu principal.\n")
                
            opcao_secundaria = input("Informe a opção desejada: ")
            
            print(f"Você escolheu a opção: {opcao_secundaria}")
            if opcao_secundaria == "1":
                print("\n===== INCLUINDO =====\n\n"
                    "Inclusão concluida...")
            elif opcao_secundaria == "2":
                print("\n===== LISTANDO =====\n\n"
                    "Listagem concluida...")
            elif opcao_secundaria == "3":
                print("\n===== ATUALIZANDO =====\n\n"
                    "Atualização concluida...")
            elif opcao_secundaria == "4":
                print("\n===== EXCLUINDO =====\n\n"
                    "Exclusão concluida...")
            elif opcao_secundaria == "9":
                print("\n===== VOLTANDO AO MENU PRINCIPAL =====\n")
                break
            else:
                print("Opção inválida, digite novamente\n")