'''Escreva um programa que cria uma lista de números inteiros e exibe os números pares da lista.'''
def  numeros_pares(lista):
    par = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par

numeros = [1,4,5,6,9,11,12,13,14]
print(f'Os números pares na lista são {numeros_pares(numeros)}')