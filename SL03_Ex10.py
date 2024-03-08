'''Escreva um programa que cria uma lista de números inteiros e remove todos os números repetidos,
exibindo a lista resultante.'''
def remover_repeticao(lista):
    nova_lista = []
    for n in lista:
        if n not in  nova_lista:
            nova_lista.append(n)
        else:
            numeros.remove(n)
    return nova_lista 
numeros = [1, 2, 3, 4, 4, 6, 7, 8,  8]
print("Lista original:", numeros)
print("A lista sem repetição é:", remover_repeticao(numeros))
