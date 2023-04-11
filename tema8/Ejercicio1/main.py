#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
def crear_archivo(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        archivo.write('Este es mi archivo\n')
        archivo.write('Aqui puedo escribir varias lineas\n')
        archivo.write('Esta es la ultima linea\n')

def listar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)

def actualizar_archivo(nombre_archivo, nueva_linea):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(nueva_linea + '\n')

mi_archivo = 'tema8/Ejercicio1/mi_fichero.txt'

crear_archivo(mi_archivo)
listar_archivo(mi_archivo)
actualizar_archivo(mi_archivo, "Añado nueva linea")
listar_archivo(mi_archivo)