ano = float(input("Introduce un año: "))
if (ano % 4 == 0) and (ano % 100 != 0):
    print(ano," Es bisiesto")
elif(ano % 100 == 0) and (ano % 400 == 0):
    print(ano," Es bisiesto")
else:
    print(ano," No es bisiesto")