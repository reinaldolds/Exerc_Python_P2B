'''Escreva um programa que cria uma lista de strings
 e exibe a mais longa palavra da lista.'''
def palavra_longa(lista):
    mais_longa = []
    for palavra in lista:
        if len(palavra) > len(mais_longa):
            mais_longa = palavra
    return mais_longa
frutas = ['banana', 'kiwi', 'batatas','uva','manga']
print(palavra_longa(frutas))