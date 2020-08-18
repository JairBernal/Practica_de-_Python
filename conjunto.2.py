#Conjuntos
a = {1, 2, 3} #Se puede omiter el SET por llaves
b = {3, 4, 5}

#Union de conjuntos
#Al momneto de imprimir mostrara los elelemntos que no se repitan
# por tal razon tomo el elemnto del conjunto A y el elemnto del conjunto B
#lo emite
c = a | b
print(c)
#Interseccion de conjuntos
d = a & b
d = (d)
#Diferencia de conjuntos
e = a - b
print(e)
#Diferencia simetrica
f = a ^ b
print(f)
#Saber si un conjunto es subconjunto de otro en 
#este caso del primer conjunto que se encuentra en 
#la linea 2
g = {1,2,3,4,5}
print(a.issubset(g))



