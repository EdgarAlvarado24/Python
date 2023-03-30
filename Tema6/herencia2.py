class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def ver_notas(self):
        print("Nombre:",self.nombre)
        print("Nota:", self.nota)
        
    def evaluar_notas(self):
        if self.nota >= 10:
            print("Haz Aprobado")
        else:
            print("Haz Reprobado")

estudiante = Alumno("Edgar", 9)
estudiante2 = Alumno("Maria",20)

estudiante.ver_notas()
estudiante.evaluar_notas()

estudiante2.ver_notas()
estudiante2.evaluar_notas()