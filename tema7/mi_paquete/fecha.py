import datetime

hora_actual = datetime.datetime.now()
hora = hora_actual.hour
hora_formateada = hora_actual.strftime('%-I:%M%p')

if hora > 7:
    print(f"Son las {hora_formateada} es hora de ir a casa")
else:
    print(f"Son las {hora_formateada} Hay que seguir trabajando")
