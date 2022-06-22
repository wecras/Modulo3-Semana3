from sre_constants import JUMP
import string


mensagem_criptografada =  ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']

codigo_letra = 0
palavra =''
lista = []
desc = ''
palavra_final =''

for codigo_letra in mensagem_criptografada:
    if codigo_letra !='-1':

         
        palavra += codigo_letra
    else:

        lista.append(palavra)
        palavra = ''
    
for desc in lista:
    
    palavra_final += chr(int(desc))
      
print(palavra_final)

 


