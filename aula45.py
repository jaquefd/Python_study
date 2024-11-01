"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Luiz' #iterável
iteratador = iter(texto) #iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except Stopteration:
        break

for letra in texto:
    print(letra)