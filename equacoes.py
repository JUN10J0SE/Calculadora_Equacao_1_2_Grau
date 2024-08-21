#biblioteca
import math

#funcao menu
def mostrar_menu():
    print('1 - Calcular equacao de 1º grau.')
    print('2 - Calcular equacao de 2º grau.')
    print('3 - Sair do Programa.')

#equacao do 1ª grau com Lambda
calcular_grau_1 = lambda a,b: -b/a

#equacao do 2º grau. Usuario informa a,b,c para chagar a X. Porem qualquer return so retorna um valor, mas equacao de 2 grau pode retornar ate 3.
def calcular_grau_2(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta < 0:
        return 'Equação não possui raizes reais.'
    elif delta == 0:
        return f'Valor de x é {(-b)/(2*a)}'
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta)/(2*a)  #return encerra a funcao o ''yild'' nao encerra ele pausa continua trazendo valores de onde pausou
        x2 = (-b - raiz_delta)/(2*a)
        yield f'Valor de x1: {x1}.'
        yield f'Valor de x2: {x2}.' #a virgula foi setada aqui por o compilador sugeriu pois estava dando linha vermelha.



