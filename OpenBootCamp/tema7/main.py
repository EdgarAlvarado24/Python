#Para utilizar un modulo primero debes importarlo
import mi_paquete.operaciones as op
from mi_paquete import conversiones as co

print(op.suma(1,3))
print(op.resta(1,3))
print(op.multiplicacion(1,3))
print(op.division(1,3))

print(co.metros_a_pies(100))
print(co.pies_a_metros(100))
print(co.fahrenheit_a_celsiues(28))
print(co.celsius_a_fahrenheit(28))