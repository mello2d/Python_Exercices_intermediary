valor_hora_aula = float(input("Informe o seu valor por hora: "))
numero_horas = int(input("Informe o número de horas aula: "))
descontos = float(input("Informe os descontos: "))

salario_liquido = (valor_hora_aula * numero_horas) - descontos

print(f"O salário líquido é: {salario_liquido}")
