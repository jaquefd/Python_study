"""
LIstas em Python
Tipo list - Mutável
Suporta vários valçores de qualquer tipo
conhecimento reutilizaveis - indices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item ao índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
     + - concatena listas
Create Read Update  Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
"""
AULA 81
lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)
"""
"""Aula 82 - extensão da aula listas
 lista.clear()
lista.insert(100, 5)
print(lista[4])
"""
"""
Aula 83 - extend e +

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
"""
"""
Aula 84 - Cuidado com dados mutáveis (list e copy)
= - copiado valor (imutáveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()


lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)