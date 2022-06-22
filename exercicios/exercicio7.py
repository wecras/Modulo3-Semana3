valor=float(input("digite o valor"))
vistadinheiro= valor * 0.85
vistacredito= valor * 0.90

forma_de_pagamento=input("informe o metodo  de  pagamento, sendo [a vista ou parcelado] :")

if forma_de_pagamento in ['a vista','vista','A Vista','A VISTA','A vista']:
    tipo_de_cartao=input("deseja pagar no dinheiro, ou cartão de credito? :")

    if tipo_de_cartao in ['dinheiro','Dinheiro','DINHEIRO']:
        print("o valor a ser pago junto ao descontos referente ao pagamento em dinheiro é de", vistadinheiro,"R$")
    else:
        print("o valor a ser pago junto ao descontos referente ao pagamento em credito é de", vistacredito,"R$")
else:
    parcelas=int(input("informe em quantas vezes deseja parcelar, lembrando que até 2x nao cobramos juros! :"))
    if parcelas ==2:
        duasvezes= valor / 2
        print("você devera pagar ",parcelas," parcelas de ",duasvezes,"R$" )
    else:
        maisdeduas= valor * 0.10
        mais_de_duas_vezes= valor + maisdeduas
        total_maior_que_duas= mais_de_duas_vezes / parcelas
        print("voce devera pagar ",parcelas," parcelas de ", total_maior_que_duas,"R$")



    



    


    

    


