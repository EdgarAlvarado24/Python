# Ejercicio de estructuras de control de flujo:
# Escribe un programa que pregunte al usuario su edad y que imprima un mensaje que diga "Eres mayor de edad" si su edad es mayor o igual a 18, y "Eres menor de edad" si su edad es menor que 18.

edad = int(input('Cual es tu edad: '))

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')