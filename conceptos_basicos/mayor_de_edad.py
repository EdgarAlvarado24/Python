# 1. Ejercicio de variables y entrada de usuario:
# Escribe un programa que pregunte al usuario su nombre, año de nacimiento y año actual, y que luego calcule y muestre por pantalla su edad. Además, si su edad es mayor o igual a 18, el programa debe imprimir un mensaje que diga "Eres mayor de edad", de lo contrario, debe imprimir "Eres menor de edad".

nombre = input('Cual es tu nombre?: ')
año_nacimiento = int(input('En que año naciste?: '))
año_actual = int(input('En que año estamos?: '))

edad = año_actual - año_nacimiento

if edad >= 18:
    print(f"Hola {nombre} eres mayor de edad y tienes {edad} años")
else:
    print(f"Hola {nombre} eres menor de edad y tienes {edad} años")

#2. Ejercicio de estructuras de control de flujo:
# Escribe un programa que pregunte al usuario su edad y nombre, y que luego imprima un mensaje que diga "Hola [nombre], eres mayor de edad" si su edad es mayor o igual a 18, y "Hola [nombre], eres menor de edad" si su edad es menor que 18.