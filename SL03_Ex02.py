'''Escreva um programa que cria uma lista de
 nomes e exibe o número total de nomes na
  lista.'''
def main():
    quantidade = 0
    lista_nomes = ["João", "Ana", "Maria", "Paulo", "Pedro", "Antônio"]
    for i in lista_nomes:
        quantidade += 1

    print(40 * "_")
    print("Primeiro Ex:")
    print(quantidade)
    print(40 * "_")

if __name__ == "__main__":
    main()

lista_nomes = ["João", "Ana", "Maria", "Paulo", "Pedro", "Antônio"]
quant = len(lista_nomes)
print(40*"_")
print("Segundo Ex:")
print(quant)
print(40*"_")