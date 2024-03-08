'''Escreva um programa que cria uma lista de números
e exibe o maior e menor número da lista.'''
lista = [19, 39, 4, 5, 8, 22, 10, 28]
maior = 0
superior = 0
menor = 2000000
inferior = 200000000
for i in lista:
    if i > maior :
       maior = i
    elif i < menor:
        menor = i

for j in range(1, len(lista)):
        superior = max(lista)
        inferior = min(lista)


print(40*"_")
print(maior)
print(inferior)
print(40*"_")
print(40*"_")
print("O maior número é: ", end="")
print(maior)
print("O menor número é: ", menor)
print(40*"_")