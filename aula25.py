"""
Interpolação básica de strings
s - string
dei - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Jaqueline'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

"""
isso é a interpolação de strings, é só voce criar a string, 
colocar % na frente da string e passar os valores para preencher
os placerolders que voce colocar.
sempre as mesmas quantidades
"""
