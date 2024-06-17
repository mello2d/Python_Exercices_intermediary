codigo = input("Insira o código: ")
quantidade = int(input("Quantidade: "))
valor = 0

if codigo == "100":
    valor = quantidade * 1.2
elif codigo == "101" :
    valor = quantidade * 1.3
elif codigo == "102" :
    valor = quantidade * 1.5
elif codigo == "103" :
    valor = quantidade * 1.2
elif codigo == "104" :
    valor = quantidade * 1.3
elif codigo == "105" :
    valor = quantidade * 1

print(valor)