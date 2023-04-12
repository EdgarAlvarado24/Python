import functools

def esImpar(numero):
    if(numero % 2 != 0):
        return numero

numeros = input("Introduce una lista de nunmeros:")
numerosLista = numeros.split(',')
numerosEnteros = [int(numero) for numero in numerosLista]
numerosPares = filter(esImpar, numerosEnteros)
print(functools.reduce(lambda a, b: a+b, numerosPares))