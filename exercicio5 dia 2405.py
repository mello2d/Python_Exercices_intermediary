nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
me = float(input("Média de exercícios: "))
ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7
if ma >= 9:
    print("A")
elif ma >= 7.5 and ma < 9:
    print("B")
elif ma >= 6 and ma < 7.5:
    print("C")
elif ma >= 4 and ma < 6:
    print("D")
else:
    print("E")

print(ma)
