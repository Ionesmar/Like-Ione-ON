def entrada_dados():
    coeficiente=quantidade=eval(input('digite um coeficiente  :  '))
    return coeficiente

def calc_delta(a,b,c):
    delta=b*b-4*a*c
    return delta
import numpy as np
def calcular_raizes(a,b,c,delta):
    if(delta<0):
        resultado='a equação não possui raizes nos números reais'
    elif (delta==0):
        x=-b/(2*a)
        resultado=f'a equação possui apenas a raiz {x}'
    else:
        x1=(-b-np.sqrt(delta))/(2*a)
        x2=(-b+np.sqrt(delta))/(2*a)
        resultado=f'a equação possui as raizes: {x1},{x2}'
    return resultado

a = entrada_dados()
b = entrada_dados()
c = entrada_dados()

delta = calc_delta(a,b,c)

resultado = calcular_raizes(a,b,c,delta)
print (resultado)
