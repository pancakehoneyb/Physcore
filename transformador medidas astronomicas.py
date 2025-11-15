#programado por Ísis Barbiere 
#Projeto Physcore 
#Objetivo do programa é simplificar transformaçoes de distancias astronomicas

import math
arquivo= open("historico.txt", "w+")
historico=[]
#funçao 
def parsecluz(parsecs):
    anos_luz = float(parsecs) * 3.262
    return anos_luz
def parsecUA(parsecs1):
    ua = float(parsecs1) * 206264.806
    return ua
def alparsec(parsecs2):
    pc = float(parsecs2) * 0.307
    return pc
def alua(parsecs3):
    uaa = float(parsecs3) * 63240 
    return uaa
def ualuz(parsecs4):
    luz = float(parsecs4) * 1.581 
    return luz
def uapraparsec(parsecs5):
    uaprap = float(parsecs5) * 4.848 


print('Olá, seja bem-vindo')
#da as opcoes 
print('Qual opção você busca?\n'
      '1 - Ver quanto vale 1 UA em parsec\n'
      '2 - Ver quanto vale 1 parsec em UA\n' 
      '3 - Ver quanto vale 1 UA em ano-luz\n'
      '4 - Ver quanto vale 1 parsec em ano-luz\n'
      '5 - Ver quanto vale 1 ano-luz em parsec\n'
      '6 - Ver quanto vale 1 ano-luz em metros\n'
      '7 - Ver quanto vale 1 UA em metro\n'
      '8 - Ver quanto vale 1 parsec em metro\n'
      '9 - Ver quanto vale 1 ano-luz em UA\n'
      '10 - Transformaçoes\n'
      '11- Fechar o programa')
while True:
    opçao_do_usuario= int(input(' digite o numero da opçao por favor\n'))
#if para cada opçao
    if opçao_do_usuario>11 or opçao_do_usuario<1:
        print(' essa opçao é invalida')
    elif opçao_do_usuario==1:
        print( 'Um UA em Parsec é = 4.848 x 10**-6 pc')
    elif opçao_do_usuario==2:
        print(' Um Parsec é = 206264.806 UA')
    elif opçao_do_usuario==3:
         print(' Um UA em ano-luz é= 1.581 x 10**-5 ano-luz')
    elif opçao_do_usuario==4:
        print('Um parsec em ano-luz é= 3.262 ano-luz')
    elif opçao_do_usuario==5:
        print(' Um ano-luz em parsec é= 0.307 pc')
    elif opçao_do_usuario==6:
        print(' Um ano-luz em metros é= 9.461 x 10**15 metros')
    elif opçao_do_usuario==9:
        print(' Um ano-luz é igual a = 63240 UA')
    elif opçao_do_usuario==7:
        print(' Um UA em metros é= 1.496 x 10**11 metros')
    elif opçao_do_usuario==8:
        print(' Um Parsec em metro é= 3.086 x 10**16 metros ')
         #se for transformaçoes
    elif opçao_do_usuario==10:
        print(' o que voce deseja?\n'
          '1- Transformar Parsec para Ano-luz\n'
          '2- Transformar Parsec para UA\n'
          '3- Transformar Ano-luz em Parsec\n'
          '4- Transformar Ano-luz em UA\n'
          '5- Transformar UA em Ano-Luz\n'
          '6- Transformar UA em Parsec')
   
        while True:
            transformacao_escolhida = int(input('Digite a opção que você deseja:\n '))  

            if transformacao_escolhida==1:
                 x = float(input('Digite o valor em parsecs que você deseja saber em anos-luz:\n '))
                 resposta = parsecluz(x)
                 print(f'O valor de {x} parsecs em anos-luz é {resposta}', file=arquivo)
                 historico.append(f'Transformação: Parsec para Ano-luz de ({x} parsecs) = {resposta}')
    
            elif transformacao_escolhida == 2:
                 y = float(input('Digite o valor em pc que você deseja saber em ua: \n'))
                 resposta2 = parsecUA(y)
                 print(f'O valor de {y} parsecs em ua é {resposta2}')
                 historico.append(f'Transformação: Parsec para UA de ({y} parsecs) = {resposta2}')

            elif transformacao_escolhida == 3:
                 z = float(input('Digite o valor em ano-luz que você deseja saber em parsec:\n '))
                 resposta3 = alparsec(z)
                 print(f'O valor de {z} anos-luz em parsec é {resposta3}')
                 historico.append(f'Transformação: Anos-luz para parsec de ({z} al) = {resposta3}')

            elif transformacao_escolhida == 4:
                 al = float(input('Digite o valor em ano-luz que você deseja saber em ua:\n '))
                 resposta4 = alua(al)
                 print(f'O valor de {al} anos-luz em ua é {resposta4}')
                 historico.append(f'Transformação: Anos-luz para ua de ({al} al) = {resposta4}')

            elif transformacao_escolhida == 5:
                 p = float(input('Digite o valor em ua que você deseja saber em anos-luz: \n'))
                 resposta5 = ualuz(p)
                 print(f'O valor de {p} ua em anos-luz é {resposta5} x 10**-5')
                 historico.append(f'Transformação: UA para Ano-luz de ({p} ua) = {resposta5}')

            elif transformacao_escolhida == 6:
                 o = float(input('Digite o valor em ua que você deseja saber em parsec: \n '))
                 resposta6 = uapraparsec(o)
                 print(f'O valor de {o} ua em parsec é {resposta6} x 10**-6')
                 historico.append(f'Transformação: UA para Parsec de  ({o} ua) = {resposta6}')


            continuar = input('Deseja fazer outro cálculo? (sim/não): \n')
            if continuar.lower() != 'sim':
                break  # Sai do loop se o usuário não desejar continuar

    continuar = input('Deseja voltar pro menu? (sim/não):\n ') 
    if continuar.lower() != 'sim':
        break  # Sai do loop se o usuário não desejar continuar         


# Mostrar o relatório
print('\nRelatório das operações:')
for operacao in historico:
    print(operacao)

