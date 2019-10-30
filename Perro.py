class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print("soy un fantasma")
        else:
            pass    

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU,GUAU")
        else:
            print("Guau,Guau")
    
    def __str__(self):
        return "perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = True
        
#         sobreescribir la instancia
    def __str__(self): 
        return "perro de Asistencia {}".format(self.amo)
    
    def pasear(self):
        return " {} ayudo a mi dueño {} a pasear ".format(self.nombre, self.amo)
    
    def ladrar(self):
        if self.trabajando:
            print("Shhhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor