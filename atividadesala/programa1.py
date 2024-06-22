def pedir_nota():
    while True:
        try:
            nota = float(input("Digite uma nota entre 0 e 10: "))
            if 0 <= nota <= 10:
                print("Nota válida! Você digitou:", nota)
                break
            else:
                print("Valor inválido. A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

pedir_nota()

