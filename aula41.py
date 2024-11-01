""" while/else
* toda vez que encontra a palavra break, o else não é executado.
* toda vez que o laço vai até o final, else é executado
"""

string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
