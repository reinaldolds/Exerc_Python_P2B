'''Escreva um programa que cria uma lista de palavras e exibe a quantidade de palavras que começam
com a letra 'A'.'''

def achar_palavras(lista):
    palavras_iniciaA = []
    for palavra in lista:
        if palavra.startswith('A') or palavra.startswith('a'):
            palavras_iniciaA.append(palavra)  
    return palavras_iniciaA

minha_lista = ['Abacaxi', 'morango', 'Uva', 'Arroz', 'aluguel', 'Aplicativo']
print(achar_palavras(minha_lista))


'''def contar_palavras_com_A(lista):
    nova_lista = []
    for palavra in lista:
        if palavra.startswith('A') or palavra.startswith('a'):
            nova_lista.append(palavra)
    return nova_lista

# Cria uma lista de palavras
lista_atual = ['Avião', 'Melancia', 'Banana', 'azul', 'uva', 'Abril', 'panela']

# Chama a função contar_palavras_com_A e armazena o resultado em uma variável
palavras_com_A = contar_palavras_com_A(lista_atual)

# Exibe a quantidade de palavras que começam com a letra 'A'
print("Quantidade de palavras que começam com a letra 'A':", palavras_com_A)
'''
