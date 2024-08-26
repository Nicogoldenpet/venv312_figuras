
class Rectangulo: #Definiendo la clase Rectángulo
    def __init__(self, ancho, largo):
        self.__ancho = ancho
        self.__largo = largo
        
    #Métodos Getter y Setter de la clase
        
    def set_ancho(self, value):
        self.__ancho = value
        
    def get_ancho(self):
        return int(self.__ancho)
    
    def set_largo(self, value):
        self.__largo = value
        
    def get_largo(self):
        return int(self.__largo)
    
    #Retornando la fórmula 
    def informe_arearectangulo(self):
        return int(self.get_ancho() * self.get_largo())

    def informe_perirectangulo(self):
        return int((self.get_largo() * 2) + (self.get_ancho() * 2))
    

class Circulo: #Definiendo la clase Círculo

    __PI = 3.141592
        
    def __init__(self, radio):
        self.__radio = radio
        
    #Métodos Getter y Setter de la clase
    
    def set_radio(self, value):
        self.__radio = value
        
    def get_radio(self):
        return int(self.__radio)
    
    #Retornando la fórmula 
    def informe_areacirculo(self):
        return int((self.get_radio() ** 2) * self.__PI)

    def informe_pericirculo(self):
        return int((self.get_radio() * 2) * self.__PI)


class Triangulo: #Definiendo la clase Triángulo
        
    def __init__(self, cateto_a, cateto_b, cateto_c):
        self.__cateto_a = cateto_a
        self.__cateto_b = cateto_b
        self.__cateto_c = cateto_c
        
    #Métodos Getter y Setter de la clase

    def set_cateto_a(self, value):
        self.__cateto_a = value
        
    def get_cateto_a(self):
        return int(self.__cateto_a)
    
    def set_cateto_b(self, value):
        self.__cateto_b = value
        
    def get_cateto_b(self):
        return int(self.__cateto_b)
    
    def set_cateto_c(self, value):
        self.__cateto_c = value
        
    def get_cateto_c(self):
        return int(self.__cateto_c)
    
    #Retornando la fórmula 
    def informe_areatriangulo(self):
        s = (self.get_cateto_a() + self.get_cateto_b() + self.get_cateto_c()) / 2
        return (s * (s - self.get_cateto_a()) * (s - self.get_cateto_b()) * (s - self.get_cateto_c())) ** 0.5

    def informe_peritriangulo(self):
        return int(self.get_cateto_a() + self.get_cateto_b() + self.get_cateto_c())
