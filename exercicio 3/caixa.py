saque = int(input("Insira o valor a ser sacado : R$"))
total = saque
cedula = 100
quantidade_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        quantidade_cedula += 1

    else:
        if quantidade_cedula >0:


            print(f'total de {quantidade_cedula} cedulas de {cedula}R$ ')
            
        if cedula == 100:
            cedula = 50

        elif cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        quantidade_cedula= 0

        if total == 0:

            break 