# Ejercicio de funciones:
# Escribe una función que calcule el promedio de una lista de números.

numeros = input('Cual es el promedio de estos numeros: ')

lista_numeros = [int(num) for num in numeros.split(',')]

#print(lista_numeros)

def promedio(lista_numeros):
    promedio = sum(lista_numeros)/len(lista_numeros)
    return print(promedio)

promedio(lista_numeros)