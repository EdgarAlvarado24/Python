
print("Introduce tu peso en kg?")
peso = float(input())
print("Introduce tu altura en m")
altura = float(input())
indiceMasaCorporal = peso // (altura)**2

if(indiceMasaCorporal<= 18.5):
        print("Bajo de peso: " + str(indiceMasaCorporal)) 
elif(indiceMasaCorporal > 18.5 and indiceMasaCorporal <= 24.9):
        print("Normal: " + str(indiceMasaCorporal))
elif (indiceMasaCorporal > 25 and indiceMasaCorporal <= 29.9):
        print("Sobrepeso: " + str(indiceMasaCorporal))
else:
        print("Obesidad: " + str(indiceMasaCorporal))
