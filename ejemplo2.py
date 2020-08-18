

materias = []
num_materias = int(input("Numero de materias >>"))

for num in range (num_materias):
    name_materia = input("Materia >>")
    materias.append(name_materia)
print(f"""Yo estudio {materias}", donde {materias}
es cada una de las asignaturas de la lista""")
