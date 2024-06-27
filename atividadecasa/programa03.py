num_cds = int(input("Digite a quantidade de CDs na coleção: "))
total_investido = 0
for i in range(num_cds):
    valor_cd = float(input(f"Digite o valor pago pelo CD {i + 1}: "))
    total_investido += valor_cd
valor_medio = total_investido / num_cds
print(f"Valor total investido: R$ {total_investido:.2f}")
print(f"Valor médio gasto por CD: R$ {valor_medio:.2f}")
