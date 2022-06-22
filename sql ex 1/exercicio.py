from distutils.util import execute
import sqlite3

conexao = sqlite3.connect('exx.sqlite3')

cursor = conexao.cursor()

sql = '''
create table pedido(
    id int not null,
    nome varchar(100),
    data varchar(20),
    categoria varchar(100),
    estatus_de_conclusao varchar(255),
    primary key (id)
) 

'''
cursor.execute (sql)
conexao.commit()
conexao.close