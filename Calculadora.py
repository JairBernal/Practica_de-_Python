while True:        
    print("""
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir""")

    opcion = int(input("Opcion >>"))

    if opcion >= 1 and opcion <= 4:
        print(f"Ingrese dos numeros: ")
        num_1 = float(input())
        num_2 = float(input())

        if opcion == 1:
            resultado = num_1 + num_2
            print(f"El resultado de la suma es {resultado}")

        elif opcion == 2:
            resultado = num_1 - num_2
            print(f"El resultado de la resta es {resultado}")

        elif opcion == 3:
            resultado =num_1 * num_2
            print(f"El resultado de la multiplicacion es {resultado}")

        else:
            resultado = num_1 / num_2
            print(f"El resultado de la division es {resultado}")
        
        
        exit()
    
    else:
        print("Vuelva pronto")  
