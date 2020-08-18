"""Calcular"""

radio= float(input('Escribre el radio:  '))
pi= 3.1416
area = pi * radio **2
longitud = 2 * pi * radio

print(f"El area es: {area:.2f} y la longitud es: {longitud:.3f}")

""" Sentencia if"""

numero = int(input("Dame el numero: "))

if numero>10:
    print("El numero es mayor a 10")
elif numero==10:
    print("El numero es 10")
else: 
    print("El numero es menor a 10")


"""Mayor de 3  numeros"""

num= int(input("Escribe el numero:  "))
num1= int(input("Escribe el numero:  "))
num2= int(input("Escribe el numero:  "))

if num>num1 & num>num2:
    print("El numero mayor es: {num}")
    if num1>num & num1>num2:
        print("El segundo numero es mayor {num1}")
        if num2>num & num2>num1:
            print("El tercer numero es myaor {num2}")
else
    else:
        else:




