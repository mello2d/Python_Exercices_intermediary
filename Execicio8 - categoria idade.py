idade = int(input("Informe a idade: "))

if idade >= 5 and idade <= 7:
    print(f"Sua idade é {idade} e a categoria é Infantil A")

elif idade >= 8 and idade <= 10:
    print(f"Sua idade é {idade} e a categoria é Infantil B")

elif idade >= 11 and idade <= 13:
    print(f"Sua idade é {idade} e a categoria é Juvenil A")

elif idade >= 14 and idade <= 17:
    print(f"Sua idade é {idade} e a categoria é Juvenil B") 

else:
    print(f"Sua idade é {idade} e sua categoria é +18") 
