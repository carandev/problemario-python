estudiantes_perdidos = 0

while True:
    codigo_estudiante = int(input("Código del estudiante: "))
    if codigo_estudiante == 0:
        break

    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    nota_3 = float(input("Nota 3: "))

    nota_final = (nota_1 + nota_2 + nota_3) / 3

    if nota_final < 3.0:
        estudiantes_perdidos += 1

    print(
        f'La nota final del estudiante con el código {codigo_estudiante} es {nota_final:.2}')

print(f'{estudiantes_perdidos} estudiantes perdieron la materia')
