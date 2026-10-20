print("Dados de Salário e Variáveis")
funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Digite seu salário bruto: ").replace(",","."))
#x = salario_bruto*0.11
#y = salario_bruto*0.9
#z = salario_bruto*0.8


#INSS
if salario >= 3000:
    inss = salario * 0.11
elif salario >= 2000:
    inss = salario * 0.09
else:
    inss = salario * 0.08
           

 #VALE TRANSPORTE
if salario >= 2000:
    vale = salario *0.06
else:
    vale = salario *0.5

if salario >= 3000:
        bonus = 300
else:
    bonus = 200


#CARGO
if salario >= 3000: 
    cargo = "Acionista"
elif salario >= 2000:
    cargo = "Gerente"
else: 
    cargo = "Vendedor"

salarioliquido = salario - (inss + vale) + bonus

print(f"Nome:  {funcionario}")
print(f"Salário Bruto: R${salario:.2f}".replace(".",","))
print(f"INSS: R${inss:.2f}")
print(f"Vale Transporte: R${vale:.2f}".replace(".",","))
print(f"Bonus: R${bonus:.2f}")
print(f"Cargo:  {cargo}")
print(f"Salário Liquido: R${salarioliquido:.2f}".replace(".",","))


     



