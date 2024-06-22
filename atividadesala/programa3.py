def encontrar_maior_numero():
    numeros = []
    for i in range(5):
        numero = float(input("Digite o {}º número: ".format(i + 1)))
        numeros.append(numero)
        maior_numero = max(numeros)
        print("O maior número é:", maior_numero)
encontrar_maior_numero()
