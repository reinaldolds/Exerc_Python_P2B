'''Escreva um programa que cria uma lista de
 números inteiros e exibe a média dos números
  da lista.'''
import random

numero = [random.randint(1, 100) for x in range(5)]
'''def calcular():
    soma = 0
    media = 0
    contador = 0
    print(numero)
    print(40*"_")
    for i in numero:
        soma += i
        contador += 1

    media = soma/contador
    print(media)

calculo = calcular()
print(calculo)
'''
total = sum(numero)
media = total/len(numero)
print(40*"-")
print(numero)
print(f'A média dos números é: {media}')
print(40*"-")




