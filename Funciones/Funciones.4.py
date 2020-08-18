""" Realiza una funcions llamada area_rectangulo (base, altura)que devuelva el area
del rectangulo a partir de una base y una altura. Calcula el área de un rectangulo
de 15 de base y 10 de altura: """

base = int(input("Base: "))
altura = int(input("Altura: "))

def area (x, y):
    return x * y

resultado = area (base, altura)
print(f"El area es {resultado}")


base = int(input("Base: "))
altura = int(input("Altura: "))

def area (x = 15, y= 10):
    return x * y

resultado = area (base, altura)
print(f"El area es {resultado}")