def atras(segundos):
    segundos -= 1
    if segundos > 0:
        print(segundos)
        atras(segundos)#Aqui se encuentra la recursividad
    else:
        print ("Tiempo terminado")
atras(11)