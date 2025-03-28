# Questão 1
# vendas_funcionarios = [2800, 3200, 1500, 4000, 5000, 1000, 3500]

# meta = 3000
# valor_bonus = 0.05


# for total_vendas in vendas_funcionarios:
#     if total_vendas > meta:
#         bonus = total_vendas * valor_bonus
#     else:
#         bonus = 0
#     print(f"R$ {bonus}")

# Questão 2
# vendas_diarias = [2000, 3000, 2500, 4000, 1800, 5000, 2700]

# meta = 2500
# dias_acima = 0

# for dias in vendas_diarias:
#     if dias > meta:
#         dias_acima += 1

# print(dias_acima)

# Questão 3
# vendas_vendedores = [1500, 2500, 1800, 3200, 4000, 1200, 2800]

# meta = 2000
# bonus = 0.08

# for vendas in vendas_vendedores:
#     if vendas > meta:
#         comissão = vendas * bonus
#     else:
#         comissão = 0
#     print(f"O valor da sua comissõ é: {comissão}")

# Questão 4
# lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

# meta = 1200
# vendas_acima = 0

# for vendas in lista_vendas:
#     if vendas > meta:
#         vendas_acima += 1 

# print(vendas_acima)

# Questão 5
# lista_vendas = [1000, 500, 800, 1500, 2000, 2300]
# meta = 1200
# percentual_bonus = 0.1
# bonus_extra = 50

# for vendas in lista_vendas:
#     if vendas > meta:
#         bonus = vendas * percentual_bonus
#     elif vendas >= 2000:
#         bonus = 50 + (vendas * percentual_bonus)
#     else:
#         bonus = 0
#     print(f"O valor final do bônus é: {bonus}")

# Questão 6
lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

maior_valor = lista_vendas[0]       

for lista_vendas in lista_vendas:
    if lista_vendas > maior_valor:
        maior_valor = lista_vendas

print(f"O maior valor é {maior_valor}")
