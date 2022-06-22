
def numero(atual= 10):
    if atual >0:
        print (atual)
        numero (atual - 1)
    
    else:
        print("fim")



numero(int(input("digite um numero :  ")))