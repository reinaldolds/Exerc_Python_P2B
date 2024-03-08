'''Escreva um programa que cria uma lista de números inteiros e exibe os números ímpares da lista.'''
import random
def  numeros_impares(lista):
    impar = []
    for i in lista:
        if i % 2 != 0:
            impar.append(i)
    return impar

numeros = [random.randint(1, 20) for  _ in range(6)]
print("Lista de Números Inteiros", numeros)
print(f"Os números ímpares são {numeros_impares(numeros)}")