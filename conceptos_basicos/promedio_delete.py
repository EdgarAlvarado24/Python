# 3. Ejercicio de funciones:
# Escribe una función que calcule el promedio de una lista de números, pero que además elimine el número más alto y el más bajo antes de calcular el promedio.

lista_numeros = [130,420,500,210,110]

def order_lista_numeros(array):
    array.sort()
    return array

order_lista_numeros(lista_numeros)

def calcular_promedio(array):
    array.pop(0)
    array.pop(len(array) - 1)

    promedio = sum(array)/len(array)
    return promedio

print(calcular_promedio(lista_numeros))