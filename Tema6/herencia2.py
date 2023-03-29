class Alumno():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_nota(self):
        return self._nota
    
    def set_nota(self, nueva_nota):
        self._nota = nueva_nota

estudiante = Alumno("Edgar", 10)

estudiante.set_nombre("Juan")
print(estudiante.get_nota())
estudiante._nota = 20
print(estudiante._nombre)
print(estudiante._nota)