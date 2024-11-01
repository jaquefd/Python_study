# Operadores in e not in
#Strings são iteráveis
#Iteráveis é algo que pode navegar intem por item
# 0 1 2 3 4 5 6 7 8 
# J a q u e l i n e
# -6-5-4-3-2-1
nome = 'Jaqueline'
#print(nome[2])
#print(nome[-4])
#print('a' in nome)
#print('z' in nome)
#print('ine' in nome)
#print(10 * '-')
#print('a' not in nome)
#print('z' not in nome)
#print('ine' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')