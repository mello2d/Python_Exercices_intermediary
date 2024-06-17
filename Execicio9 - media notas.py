n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
m = (n1 + n2) / 2

if m >= 7:
     print("Aprovado")
else:
    r = float(input("Informe a nota da recuperação: ")) 
    rm = (m + r) / 2
    if rm >= 6:
      print("Aprovado")
    else:
      print("Reprovado")
     



