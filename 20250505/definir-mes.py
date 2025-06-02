# Ejercicio: Tenemos que ingresar por pantalla un <string con la fecha en formato ISO, por ejemplo
# "2025050", identificar el mes en el que se encuentra en este caso mayo.

# resolucion 1:
# fecha = input("Ingrese fecha de formato AAAAMMDD:")
# meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

# if len(fecha) == 8 and fecha.isdigit():
#     mes_ingresado = int(fecha[4:6])
#     if 1 <= mes_ingresado <= 12:
#         print(f"El mes es {meses[mes_ingresado - 1]}")
#     else:
#         print("la fecha ingresada NO tiene el formato correspondiente...")

# resolucion 2:
