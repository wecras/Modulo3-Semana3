import sqlite3

conexao = sqlite3.connect('aoo.sqlite3')

cursor = conexao.cursor()

sql = '''
create table evento(
    id int not null,
    titulo varchar (100),
    data varchar (20),
    local varchar (255),
    organizador_id not null,
    primary key (id),
    foreign key (organizador_id) references organizador (id)
)

'''
cursor.execute (sql)
conexao.commit()
conexao.close
