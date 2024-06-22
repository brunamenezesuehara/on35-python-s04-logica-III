def pedir_credenciais():
    while True:
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        if senha == usuario:
            print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")
        else:
            print("Credenciais válidas! Nome de usuário:", usuario, "Senha:", senha)
            break
pedir_credenciais()
