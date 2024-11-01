# Operadores lógicos
# and (e) or (ou) not (nao)
# or -  Qualquer condição verdadeira avalia
# toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro, 
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que nós ja vimos)
# 0 0.0 '' False
# Também existe o tipo NOne que é 
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada:
    print('Entrar')
else:
    print('Sair')

 #Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
