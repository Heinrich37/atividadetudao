def menu():
    while True:
        print("\n---------------SISTEMA DE OFICINA MECANICA---------------")
        opção = input("1 - Cadastro\n2 - Consulta\n3 - Edição\n4 - Exclusão\n5 - Sair\nInforme a opção: ")

        if opção == "1":
            menu_cadastro()
        if opção == "2":
            menu_consulta()
        if opção == "3":
            menu_edição()
        if opção == "4":
            menu_exclusão()
        if opção == "5":
            print("Encerrando o programa")
            break
        else:
            print("Opção invalida")
menu()
def menu_cadastro():
    try:
        print("\n---------------CADASTRO DE CLIENTE---------------")
        nome = input("Nome do cliente: ")
        cpf = input("")
