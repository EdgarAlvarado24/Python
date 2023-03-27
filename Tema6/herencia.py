class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

    def getColor(self):
        return self._color
    
    def setColor(self, nuevo_color):
        self._color = nuevo_color

    def getRuedas(self):
        return self._ruedas
    
    def setRuedas(self, numero_ruedas):
        self._ruedas = numero_ruedas

    def getPuertas(self):
        return self._puertas
    
    def setPuertas(self, numero_puertas):
        self._puertas = numero_puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cinlindrada):
        super().__init__(color, ruedas, puertas)
        self._velocidad = velocidad
        self._cilindrada = cinlindrada

    def getVelocidad(self):
        return self._velocidad
    
    def setVelocidad(self, nueva_velocidad):
        self._velocidad = nueva_velocidad

    def getCilindrada(self):
        return self._cilindrada
    
    def setCilindrada(self, nueva_cilindrada):
        self._cilindrada = nueva_cilindrada

coche = Coche('Rojo', 4, 2, "300km", "Alta")

print(f"Velocidad: {coche.getVelocidad()}, \nCilindrada: {coche.getCilindrada()}, \nColor: {coche.getColor()}, \nRuedas: {coche.getRuedas()}, \nPuertas: {coche.getPuertas()}")

