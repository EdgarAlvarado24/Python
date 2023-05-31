import datetime

hora_actual = datetime.datetime.now()
hora = hora_actual.hour
minutos = hora_actual.minute
hora_formateada = hora_actual.strftime('%-I:%M%p')

if hora > 19:
    print(f"Son las {hora_formateada} es hora de ir a casa")
else:
    print(f"Quedan {19-hora}H:{minutos}m para salir del trabajo")