student_code = input('Código del estudiante: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

final = (n1 + n2 + n3) / 3

print(f'{student_code}: {final:.2}')
