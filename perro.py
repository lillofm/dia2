class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
            
    def __str__(self):
        print "Soy el perro{}".format(self.nombre)
        
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self,nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False#lo hemos hecho privado poniendo elguion en trabajando
        
    def __str__(self):
        return "Perro deasistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.__trabajando:#aqui tambien lo tengo que acabiar por que no puedo llamar a trabajando
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
    
    def trabajando(self, valor =None):  #hacemos trabajando privado y creamos esta función
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
        