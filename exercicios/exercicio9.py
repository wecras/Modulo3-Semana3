import hashlib
import json


codificado = []
str = ""
mensagem = "HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ "

mensagem= mensagem.lower()

chave = 3

for letra in mensagem:
	passou = ord(letra)
	if passou >=123 and passou <=127:
		letra1 = chr(passou)
		codificado.append(letra1)
		
	elif passou >= 32 and passou <=64:
		letra1 = chr(passou)
		codificado.append(letra1)
	elif (passou - chave) < 97 :
		certo=((passou - chave) + 26)
		letra1 = chr(certo)
		codificado.append(letra1)
	else :
		letra1 = chr(passou - chave)
		codificado.append(letra1)


mensagemcodificada = (str.join(codificado))

print (hashlib.sha1((mensagemcodificada).encode('utf-8')).hexdigest())

print(mensagemcodificada)