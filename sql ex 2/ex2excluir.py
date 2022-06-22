idd = input("insira o id que deseja deletar")
import sqlite3


import sqlite3
conexao = sqlite3.connect ('exercicio2.sqlite3')
cursor = conexao.cursor()

sql = 'DELETE FROM Fornecedor WHERE id = (?)'
valor =[idd]


cursor.execute(sql,valor)

conexao.commit()

conexao.close()
