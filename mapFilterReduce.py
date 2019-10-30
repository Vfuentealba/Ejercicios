from functools import reduce

def sumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
    return resultado

def sumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor*2
    return resultado

def ProductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor 
    return resultado

def dobles(n):
    return n * n

lista = [1, 3, -1, 9, 15]
listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(dobles, lista)

def esPar(x):
    return x % 2 == 0

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = map(esPar, lista)

sumatorio = reduce(lambda x, y: x + y, lista)
suma100 = reduce(lambda x, y: x + y, range(101))

l = lista[:]
l.insert(0,0)

 