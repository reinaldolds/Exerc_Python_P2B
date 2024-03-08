'''Escreva um programa que cria uma lista de
 números inteiros e exibe a soma de todos os
 números da lista.'''
import random
'''def Soma():
    total = 0
    ls_num = [random.randint(1, 100) for x in range(10)]
    print(f'Essa é a lista:')
    print(f'{ls_num}')
    for i in ls_num:
        total += i

    print(40*"*_*")
    print(f'Aqui é a soma:', total)
    print(40 * "*_*")

if __name__ == "__main__":
    Soma()
'''
lista_num = [random.randint(1, 100) for x in range(5)]
total2 = 0
cont = len(lista_num)
print(lista_num)

for j in lista_num:
    total2 += j

print(40*"_")
print(len(lista_num), " A quantidade vezes.")
print(f"O segundo resultado da soma é: {total2}")
print(40*"_")