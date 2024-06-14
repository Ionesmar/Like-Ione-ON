def calcule_menor (lista):
    menor=lista[0]
    for elem in lista:
        if elem<menor:
            menor=elem
    return menor

lista= [5,6,3,23,6,7,8,4]
menor_elem =calcule_menor(lista)
print(f'O menor valor da lista é : {menor_elem}')
'''a,b = 5,10
print (a*b)'''