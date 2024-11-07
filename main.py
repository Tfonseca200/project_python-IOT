from resources.Consulta import consulta_produto, conectar_api

while True:
    print("\nMenu:")
    print("1. Consultar produto")
    print("2. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1": 
        dados = conectar_api()
        consulta_produto(dados)

    elif opcao == "2":
        break
    else:
        print("Opção inválida.")