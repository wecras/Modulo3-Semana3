import string


sexo=input("informe seu sexo,sendo Homem ou Mulher :")
altura= float(input("informe sua altura, exemplo 1.74 : "))
homem= 72.7 * altura - 58 
mulher= 62.1 * altura - 44.7
if sexo in ['H','h','HOMEM','homem','Homem']: 

    print("seu peso ideal é :",round (homem,2))

else:
     print("seu peso ideal é :",round (mulher,2))