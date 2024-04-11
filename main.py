"""
    Anthony Maia Dolberth
    Superior de Tecnologia em Análise e Desenvolvimento de Sistemas
"""

estudantes = []

while True:
    print("----- MENU PRINCIPAL -----\n\n"
    "(1) Gerenciar estudantes.\n"
    "(2) Gerenciar professores.\n"
    "(3) Gerenciar disciplinas.\n"
    "(4) Gerenciar turmas.\n"
    "(5) Gerenciar matrículas.\n"
    "(9) Sair.\n")
    
    opcao = int(input("Informe a opção desejada: "))
    
    if opcao == 1:
        opcao_escolhida = "Estudantes"
        print(f"Você escolheu a opção: Gerenciar {opcao_escolhida}")
        opcao_escolhida = opcao_escolhida.upper()
        while True:
            print(f"\n----- [{opcao_escolhida}] - MENU DE OPERAÇÕES -----\n\n"
                "(1) Incluir.\n"
                "(2) Listar.\n"
                "(3) Atualizar.\n"
                "(4) Excluir.\n"
                "(9) Voltar ao menu principal.\n")
            
            opcao_secundaria = int(input("Informe a opção desejada: "))
            
            print(f"Você escolheu a opção: {opcao_secundaria}")
            if opcao_secundaria == 1:
                print("\n===== INCLUSÃO =====\n")
                estudante = input("Informe o nome do estudante: ")
                estudantes.append(estudante)
                print("Inclusão concluída.")
            elif opcao_secundaria == 2:
                print("\n===== LISTAGEM =====\n")
                if estudantes == []:
                    print("Nenhum estudante listado ainda.")
                for estudante in estudantes:
                    print("-- " + estudante)
                print("\nListagem concluída.")
            elif opcao_secundaria == 3:
                print("EM DESENVOLVIMENTO")
            elif opcao_secundaria == 4:
                print("EM DESENVOLVIMENTO")
            elif opcao_secundaria == 9:
                print("\n===== VOLTANDO AO MENU PRINCIPAL =====\n")
                break
            else:
                print("Opção inválida, digite novamente\n")
    elif opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        print("EM DESENVOLVIMENTO \n")
    elif opcao == 9:
        print("\nFinalizando aplicação...\n")
        break
    else: 
        print("Nenhuma opção correspondente, digite novamente\n")