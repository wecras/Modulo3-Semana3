import sqlite3
conexao = sqlite3.connect('sqltodo.sqlite3')
cursor = conexao.cursor()

pedido = input ("insira o nome do pedido")

sql = (
    'insert into'
)