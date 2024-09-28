nome_completo = input("Digite seu nome completo: ")
salario_fixo = input("Digite seu salário fixo: ")
quantidade_de_vendas = input("Digite a quantidade de vendas: ")

bonus = int(float(quantidade_de_vendas) * 15) / 100
salario_total = float(salario_fixo) + float(bonus)
print (f"TOTAL = R$ {salario_total:.2f}")
