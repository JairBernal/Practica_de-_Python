"""Conjunto--> Lista de elementos desordenados donde NO SE PUEDE REPETIR
al momento de mandarlo a imprimir, los mostrara desordenadamente"""
Conjunto = set() #Se inicializa un conjunto vacio
conjunto = {1, 3.5, True, "Hola" } #Sus elementos son con llave
conjunto.add(3) #Para agregar otro elemnto al conjunto
conjunto.discard (3.5) #Elminar un elemnto
conjunto.clear() #Para liimpiar el conjunto

print(conjunto)
