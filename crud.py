# author: @baleralarissa
# date: 07/07/2022

# biblioteca
import mysql.connector

# DB connection

# Configurar campos para que o código funcione.
conn = mysql.connector.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)

cursor = conn.cursor()

# CRUD STRUCTURE
# Table: Foi criada uma tabela com o nome de products com as colunas: 'codigo', 'nome_produto', 'preco', 'quantidade'

#CREATE

codigo = input("Digite o código do produto: ")
nome_produto = input("Digite o nome do produto: ")
preco = input('Digite o valor do produto: ')
quantidade = input('Digite a quantidade em estoque: ')

cmd = f'INSERT INTO products (codigo, nome_produto, preco, quantidade) VALUES ("{codigo}","{nome_produto}", {preco}, {quantidade})'

cursor.execute(cmd)
conn.commit() 

# READ

cmd = f'SELECT * FROM products'

cursor.execute(cmd)
resultado = cursor.fetchall()
print(resultado)

# UPDATE

codigo = input("Digite o código do produto: ")
nome_produto = input("Digite o nome do produto: ")
preco = input("Digite o valor do produto: ")
quantidade = input("Digite a quantidade em estoque do produto: ")

cmd = f'UPDATE products SET nome_produto = "{nome_produto}", preco = {preco}, quantidade = {quantidade} WHERE codigo = "{codigo}"'

#DELETE

codigo = input("Digite o código do produto a ser deletado: ")

cmd = f'DELETE FROM products WHERE codigo = "{codigo}"'

cursor.execute(cmd)
conn.commit()


cursor.close()
conn.close()

