salario = float(input("Informe o salário antigo: "))
cargo = input("Informe o seu cargo: ")
codigo = int(input("Qual o código: "))

dicio = {cargo:codigo}
for cargo, valor in dicio.items():
    if cargo.capitalize() == "gerente" and valor == 101:
        novo_salario = salario + salario * 0.10
        print(f"O novo salário é: {novo_salario} \nO antigo é: {salario} \nO reajuste foi de 10%")

    elif cargo.capitalize() == "engenheiro" and valor == 102:
        novo_salario = salario + salario * 0.20
        print(f"O novo salário é: {novo_salarios} \nO antigo é: {salario} \nO reajuste foi de 20%")

    elif cargo.capitalize() == "tecnico" and valor == 103:
        novo_salario = salario + salario * 0.30
        print(f"O novo salário é: {novo_salario} \nO antigo é: {salario} \nO reajuste foi de 30%")
    else:
        novo_salario = salario + salario * 0.40
        print(f"O novo salário é: {novo_salario} \nO antigo é: {salario} \nO reajuste foi de 40%")