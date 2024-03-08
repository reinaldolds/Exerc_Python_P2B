'''Escreva um programa que cria duas listas de números inteiros e exibe os números que estão presentes
em ambas as listas.'''
import random
def  criar_lista(lista1, lista2):
    iguais = []
    for n in lista1:
        if n in lista2:
            iguais.append(n)
    return iguais

primeira = [random.randint(1, 10) for  _ in range(5)]
segunda = [random.randint(1, 10) for  _ in range(5)]
inicio = criar_lista(primeira, segunda)
print(f"A primeira lista é: {primeira}")
print(f"\nA segunda lista é: {segunda}\n")
print(f"As listas juntas é:", criar_lista(primeira, segunda))