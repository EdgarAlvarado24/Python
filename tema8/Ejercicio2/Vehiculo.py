class Vehiculo():

    marca=""
    modelo=""
    
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def get_marca(self):
        return self._marca
    
    def set_marca(self, nuevaMarca):
        self._marca = nuevaMarca

    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, nuevoModelo):
        self._modelo = nuevoModelo

    def __str__(self):
        return f"Marca:{self._marca},\nModelo:{self._modelo}"

carro = Vehiculo('Mustang', 'GT')

nuevoFichero = "tema8/Ejercicio2/mi_vehiculo.txt"

def crear_archivo(nuevoFichero):
    f = open(nuevoFichero, 'w')
    f.write(str(carro))
    f.close()

crear_archivo(nuevoFichero)

def listar_archivo(nuevoFichero):
    f = open(nuevoFichero, 'r')
    datos = f.readlines()
    f.close()
    print('Datos desde la funcion listar_fichero')
    for dato in datos:
        print(dato)

listar_archivo(nuevoFichero)