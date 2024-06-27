def gerar_fibonacci(n):
    fibonacci = [1, 1]
    for i in range(2, n):
        proximo_termo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_termo)
    for termo in fibonacci:
        print(termo, end=' ')
    print()
num_termos = int(input("Digite o número de termos da série de Fibonacci que você deseja ver: "))
if num_termos <= 0:
    print("Por favor, digite um número maior que zero.")
else:
    gerar_fibonacci(num_termos)
    
