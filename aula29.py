"""
INtrodução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'VOu dobrar o número que você digitar'
    )

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_str)
    print(f'O dobro de{numero_str} é {numero_float *2:.2f}')
except:
    print('Isso não é um número')


#if numero_str.isdigit():
#    numero_float = float(numero_str)
 #   print(f'o dobro de {numero_str} é {numero_float *2:.2f}')
#else:
#   print('isso não é um numero')
