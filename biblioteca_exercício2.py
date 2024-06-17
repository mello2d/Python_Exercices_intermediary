cadastro = []

while True:
    veiculo = {}
    veiculo["nome"] = input("Informe o nome do veículo: ")
    veiculo["ano"] = int(input("Informe a ano do veículo: "))
    veiculo["valor"] = int(input("Informe o valor do veículo: "))
    veiculo["descrição"] = input("Informe o descrição do veículo: ")
    veiculo["condição_km"] = float(input("Informe a km do veículo: "))

    cadastro.append(veiculo)
    r = input("Deseja continuar? (s/n): ").lower()
    if r == 'n':
        break
for nome_carro in cadastro:
    print (nome_carro["nome"])