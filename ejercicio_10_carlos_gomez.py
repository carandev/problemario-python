num = input('Ingresa el número a evaluar: ')
sum = 0

for letter in num:
    sum += int(letter)

print(f'La suma de los digitos es: {sum}')
print(f'El número recibido es: {num}')
