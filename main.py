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
                while True:
                    codigo = int(input("Digite o código do estudante: "))
                    nome = input("Digite o nome do estudante: ")
                    cpf = (input("Digite o CPF do estudante: "))
                    novo_estudante = {'Codigo': codigo, 'Nome': nome, 'CPF': cpf}
                    estudantes.append(novo_estudante)

                    if input("Deseja cadastrar um novo aluno? (s/n) ") == "n":
                        print("Inclusão concluída.")
                        break
            
            elif opcao_secundaria == 2:
                print("\n===== LISTAGEM =====\n")
                if len(estudantes) == 0:
                    print("Nenhum estudante listado ainda.")
                else:
                    for estudante in estudantes:
                        print(f"-- Código: {estudante['Codigo']}, Nome: {estudante['Nome']}, CPF: {estudante['CPF']}")
                print("\nListagem concluída.")

            elif opcao_secundaria == 3:
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
            
            elif opcao_secundaria == 4:
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