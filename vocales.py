"""Hallar vocal"""


vocal = input("Escribe una letra: ").lower()

if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
    print(f"La letra {vocal} es una vocal")
else: 
    print (f"La letra es una consonante")
