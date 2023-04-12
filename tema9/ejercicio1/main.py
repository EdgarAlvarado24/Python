def eliminar_espacios(cadena):
    return cadena.replace(" ", "")

def ordenar_paises(paisesRecibidos):
    listaPaises = sorted(set((paisesRecibidos.split(','))))
    paisesOrdenados = ",".join(listaPaises)   
    print('Paises Ordenados:',paisesOrdenados)

paises = eliminar_espacios(input('Introduce una lista de paises:'))
ordenar_paises(paises)