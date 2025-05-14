# Ejercicio: Tenemos que ingresar por pantalla un <string con la fecha en formato ISO, por ejemplo
# "2025050", identificar el mes en el que se encuentra en este caso mayo.

# resolucion

fecha = input("Ingrese fecha en formato AAAMMDD:")
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiempre", "octubre", "noviembre", "diciembre"]

mes_ingresado = fecha[4:6]

