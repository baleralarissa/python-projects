#Código para gerar senhas aleatórias dentro de um range de caracteres definidos pelo usuário usando a bilbioteca random

# Biblioteca
import random

print("Olá! Este é o seu gerador de senhas")

#Definindo caracteres possíveis para a senha
char = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ?!@#$%&*().,-0123456789' 

#Quantidade de senhas que o usuário quer gerar e conversão de str para int
quantidade = input("Quantas senhas você quer gerar? ")
quantidade = int(quantidade)

#Quantidade de caracteres que o usuário quer na senha e conversão de str para int
tamanho = input("Quantos caracteres você quer na sua senha? ")
tamanho = int(tamanho)

print("\nSuas novas senhas são: ")

#Laço de repetição for com função range para gerar quantidade de senhas solicitadas e com a quantidade de caracteres solicitados utilizando a função random
for senhas in range(quantidade):
    senhas = ''
    for t in range(tamanho):
        senhas += random.choice(char)
    print(senhas)
