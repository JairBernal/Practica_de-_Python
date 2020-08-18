#Programa que muestre los nuneros pares de un cierto rango
numero1 = int(input("Ingrese el primer numero: "))
numero2 = numero1
while numero2 <= numero1:
    numero2 = int(input("Ingrese el segundo numero: "))

for n in range(numero1,numero2+1):
    if n %2 ==0:
        print(n)



