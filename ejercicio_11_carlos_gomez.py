num_reverse = input('Digite el número a evaluar: ')
num_array = []

for letter in num_reverse:
    num_array.append(letter)

num_array.reverse()
num_reverse = ''

print(num_reverse.join(num_array))
