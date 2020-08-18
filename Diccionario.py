"""Coleccion --> Diccionarios"""

""" colores = {"black":"negro", "golden": "dorado" }
pirnt(colores["black"])# Hacemos referncia a la clave y nos imprime su valor
#Para agregar otro elmento seria 
colores["yellow"] = "amarillo"
print(colores)
#Para eliminar un elemento
del(colores["black"])
print(colores) """

#Ejercicio

equipo = {10: "Messi", 7: "Cristiano", 11: "Neymar"}

print(equipo.get(30," No existe"))
print(10 in equipo)# Aqui pregunta si el numero 10 existe en mi conjunto equipo
print(equipo.keys()) #Nos muestra sus claves del diccionario
print(equipo.values()) #Nos muestra el valor de las claves
print(equipo.items())#Es otra manera de mostrar los valores por separdos
print(len(equipo))#Nos dice cuantos elementos tiene el conjunto
equipo.clear()
print(equipo)#Para limpiar el conjunto