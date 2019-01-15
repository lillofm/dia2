class termometro():
    def __init__(self):
        self.__unidadM = "C"#los hacemos privados
        self.__temperatura = 0
        
    def conversor(self, temperatura, unidad):
        if unidad = "C":
            return "{}ºF".format(temperatura * 9/5 + 32)
        elif unidad == "F":
            return "{}ºC".format((temperatura -32) * 5/9)
        else:
            return "unidad incorrecta"
        
    def __str__(self):
        return "{}º{}". format(self.temperatura, self.unidadM)
    
    def unidadMedida(self, uniM):
        if uniM == None:
            return self.__unidadM
        else:
            if self.uniM == "F" or uniM == "C":
                self.__unidadM = uniM
                
    def temp (self, temperatura=None):
        if temperatura == None:
            return self.__teperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM=None):
        if uniM == None or uniM = self.unidadM:
            return self.__str__()
        else:
            return self.conversor(self, temperatura,uniM)