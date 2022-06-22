peso=float(input("insira seu peso :"))
altura=float(input("insira sua altura  :"))
imc= peso / (altura)**2

print("seu IMC é :", round (imc,2))

if imc < 18.5:
    print("voce está abaixo do peso")
if imc >= 18.5 and imc < 25:
    print("voce esta com o peso normal")
if imc >= 25 < 30:
    print("voce esta acima do peso")
if imc > 30:
    print("voce esta obeso(a)")

