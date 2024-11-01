""""
Faça um jogo para o usuario adivinhar qual
a palavra secreta.
VOcê vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuario digitar apenas uma letra.
- quando o usuário digitar uma letra, você vai conferir
se a letra digitada esta na palavra secreta-
    -se a letra digitada estiver na palavra secreta; exiba a letra; 
    -se a letra digitada não estiver na palvara secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palvra formada', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas += 1
