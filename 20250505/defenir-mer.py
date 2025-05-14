# Ejercicio: Tenemos que ingresar por pantalla un <string con la fecha en formato ISO, por ejemplo
# "2025050", identificar el mes en el que se encuentra en este caso mayo.

# resolucion

fecha = input("Ingrese fecha en formato AAAMMDD:")
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiempre", "octubre", "noviembre", "diciembre"]

mes_ingresado = int(fecha[4:6])
if 1 <= mes_ingresado <= 12:
    print(f"El mes es {meses[mes_ingresado -1]}")
else:
    print("La fecha ingresada no tiene el formato correspondiente...")
