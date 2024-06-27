print('O nome dos candidatos não são ilustrativos, apesar de parecer haha, estão entre os 60 nomes mais exóticos das últimas eleições')

def eleicao():
   
    candidatos = ["Bacural 1", "Barbie do Povo 2", "Flor da Sorte 3"]
    

    votos = {1: 0, 2: 0, 3: 0}

    try:
        num_eleitores = int(input("Digite o número total de eleitores: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
        return  

    
    for i in range(num_eleitores):
        while True:
            print(f"Eleitor {i + 1}, escolha seu candidato:")
            print("1 - Bacural 1")
            print("2 - Barbie do Povo 2")
            print("3 - Flor da Sorte 3")
            
            try:
                voto = int(input("Digite o número do candidato escolhido (1, 2 ou 3): "))
                if voto in votos:
                    votos[voto] += 1
                    break
                else:
                    print("Voto inválido! Por favor, escolha um candidato válido (1, 2 ou 3).")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro (1, 2 ou 3).")

   
    for num, nome in enumerate(candidatos, start=1):
        print(f"{nome} recebeu {votos[num]} votos.")

eleicao()