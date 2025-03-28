# Lista de valores
numeros = [10, 25, 3, 70, 45]

# Inicializando a variável para armazenar o maior valor
maior_valor = numeros[0]  # Começa com o primeiro elemento da lista

# Loop para encontrar o maior valor
for numero in numeros:
    if numero > maior_valor:
        maior_valor = numero  # Atualiza se encontrar um número maior

# Exibindo o maior valor
print(f"O maior valor da lista é: {maior_valor}")
