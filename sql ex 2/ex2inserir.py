id = input ("digite o id do Fornecedor")
nome = input ("digite o nome do  Fornecedor")
endereco = input ("digite o endereco do Fornecedor")
produto = input ("digite o produto do Fornecedor")

import sqlite3

conexao = sqlite3.connect ('exercicio2.sqlite3')
cursor = conexao.cursor()
sql= 'INSERT INTO Fornecedor (id,nome,endereco,produto) VALUES (?,?,?,?)'

valores = [id, nome, endereco, produto]

cursor.execute(sql,valores)

conexao.commit()

print('Dados inseridos com sucesso!')

conexao.close()