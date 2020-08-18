import calendar
año = int(input("Ingrese el año "))
print("Calendario de {años}")
print(calendar.calendar(año))

#Para imprimir un mes 
y = 2000
m = 2
print(calendar.month(y, m))

#Ingresar el mes que deseamos solicitar

y = int(input("Año: "))
m = int(input("Mes: "))
print(calendar.month(y, m))