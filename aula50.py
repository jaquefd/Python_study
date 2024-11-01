"""
Exercicio
Exiba os indices da lista
0 maria
1 helena
2 luiz
"""
#          0        1         2
lista = ('Maria', 'Helena', 'Luiz')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))