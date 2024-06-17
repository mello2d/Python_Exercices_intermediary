altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo: ")
m = (72.7*altura)-58
f = (62.1*altura)-44.7

if sexo == "m":
    print(f"{m:.2f}")
else:
    print(f"{f:.2f}")

