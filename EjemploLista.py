""" Realiza una funcion de separar (Lista)que tome las dos lista, una lista con numeros pares
y la otra lista con numeros impares y los separe

list = [1, 2, 3, 4, 5] 
list_2 = [11, 12, 13, 14, 15]
list_par = []
list_impar =[]
def separar(listas):
    for avanzar in list:
        if avanzar %2== 0:
            list_par.append(avanzar)
        else:
            list_impar.append(avanzar)
    return list_par, list_impar

list_par, list_impar = separar(list)
print(list_par)
print(list_impar) """



numero_maximo = int(input("Ingrese el total de numeros"))
list = int(input("Ingrese los valores: "))

list_par = []
list_impar =[]
def separar(listas):
    for avanzar in list:
        if avanzar %2== 0:
            list_par.append(avanzar)
        else:
            list_impar.append(avanzar)
    return list_par, list_impar

list_par, list_impar = separar(list)
print(list_par)
print(list_impar)
