cod = ''
estudiantes_sistemas_mayores = []

while not '0' in cod:
    cod = input('Ingresa el código del estudiante: ')
    age = int(input('Ingresa la edad del estudiante: '))
    prom = float(input('Ingresa el promedio acumulado: '))

    if age > 21 and cod == '11':
        estudiantes_sistemas_mayores.append({
            'cod': cod,
            'age': age,
            'prom': prom
        })

for student in estudiantes_sistemas_mayores:
    print('-------------- Student --------------')
    for key, value in student.items():
        print(key,value)

print(f'El total de estudiantes es: {len(estudiantes_sistemas_mayores)}')
