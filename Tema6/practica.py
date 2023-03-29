# Crear una clase Ninja y Clase Personaje, la clase ninja tendra los atributos Rango, Genin, Jounin, AMBU, Kage y numero de misiones _{a:13 b:25 c:36 : D:12}. la clase personaje tendra nombre, edad, utilizara clase ninja, pais y aldea

class Ninja():
    def __init__(self, rango, numeroDeMisiones):
        self.rango = rango
        self.numeroDeMisiones = numeroDeMisiones
    
    def getRango(self):
        return self.rango
    
    def setRango(self, nuevoRango):
        self.rango = nuevoRango

    def getNumeroDeMisiones(self):
        return self.numeroDeMisiones
    
    def setNumeroDeMisiones(self, nuevoNumeroDeMisiones):
        self.numeroDeMisiones = nuevoNumeroDeMisiones

class Personaje(Ninja):
    def __init__(self, rango, numeroDeMisiones, nombre, edad, pais, aldea):
        super().__init__(rango, numeroDeMisiones)
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.aldea = aldea

    def getNombre(self):
        return self.nombre
    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def getEdad(self):
        return self.edad
    def setEdad(self, nuevoEdad):
        self.nombre = nuevoEdad

    def getPais(self):
        return self.pais
    def setEdad(self, nuevoPais):
        self.nombre = nuevoPais

    def getAldea(self):
        return self.aldea
    def setAldea(self, nuevaAldea):
        self.nombre = nuevaAldea

naruto = Personaje("Genin", {"A":1, "B": 22, "C": 36, "D": 44}, "Naruto", 12, "Fuego", "Aldea de la Hoja")

print(f"Hola, mi nombre es {naruto.getNombre()} Soy un {naruto.getRango()} de la {naruto.getAldea()}, el cual se encuentra en el pais {naruto.getPais()}")