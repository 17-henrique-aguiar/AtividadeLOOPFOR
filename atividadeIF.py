# pague = str(input("Insira seu método de pagamento: "))

# if pague == "cartao":
#     print("Processando pagamento no cartão...")
# elif pague == "boleto":
#     print("Gerando boleto bancário...")
# else:
#     print("Método de pagamento não reconhecido.")

# idade = int(input("Digite sua idade: "))

# if idade <= 12:
#     print ("Criança")
# elif idade >= 13 and idade <= 17:
#     print("Adolescente")
# elif idade >= 18 and idade <= 59:
#     print("Adulto")
# elif idade >= 60:
#     print("Idoso")

# valor_compra = float(input("Insiro o valor da sua compra: "))

if valor_compra <= 50:
    print(f"O valor a ser pago é de R${valor_compra * 0.10}")
elif valor_compra >= 51 and valor_compra <= 150:
    print(f"O valor a ser pago é de R${valor_compra * 0.15}")
elif valor_compra >= 151 and valor_compra <= 300:
    print (f"O valor a ser pago é de R${valor_compra * 0.20}")

entrega = str(input("Qual seu tipo de entrega: "))

if entrega == "padrão":
    print("Custa R$ 10,00")
elif entrega == "expresso":
    print("Custa R$ 20,00")
else:svdvsd
    print("Opção de entrega inválida.")

# nota = int(input("insira a nota: "))

# if nota < 50:
#     print("Reprovado!")
# elif nota >= 50 and nota <= 69:
#     print("Recuperação!")
# elif nota >= 70 and nota <= 89:
#     print("Aprovado!")
# elif nota >= 90:
#     print("Aprovado com exelência!")

# tempo = str(input("Insira o tempo de permanência do veículo: "))

# if tempo s