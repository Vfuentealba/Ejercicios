def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for lx in range(1, len(l)):
        if l[lx] > m:
            m = l[lx]
    
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for lx in range(1, len(l)):
        if l[lx] < m:
            m = l[lx]
    
    return m

def media(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    suma = 0
    for valor in l:
        if l[valor] < m:
            suma += valor
    
    return suma/ len(l)

funciones = {
    'max' : maxi,
    'min' : mini,
    'med' : media
    }

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return nombre