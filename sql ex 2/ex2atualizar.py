import sqlite3


import sqlite3
conexao = sqlite3.connect ('exercicio2.sqlite3')
cursor = conexao.cursor()

sql = 'UPDATE Fornecedor SET endereco = "Rua dos Peixes, 26" WHERE id=2'


cursor.execute(sql)

conexao.commit()

conexao.close()
