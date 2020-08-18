""" Resliza una funcions llamada area_circulo(radio) que devuelva el area de un
circulo a partir de un radio. Calcula el área de un circulo de 5 de radio """
#.pow es para elevar a un exponente 
import math
radio =  float(input("Radio es"))

def area_circulo(rad):
    return (math.pow(rad, 2)) * math.pi

resultado = area_circulo(radio)
print(f"El area es {resultado:.4f}")