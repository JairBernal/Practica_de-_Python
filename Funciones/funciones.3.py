"""num_1 = int(input("Digite el primer numero"))
num_2 = int(input("Digite el segundo numero))"""

def nulos(x = None, y = None):
    if x ==None or y == None:
        print("No hay datos")
        return
    return x + y

suma = nulos(9, 17)
print(f"Suma final es: {suma}")