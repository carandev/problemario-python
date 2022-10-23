capital = float(input('Capital: '))
interes_compuesto = 0
meses = 0

while capital > interes_compuesto:
    interes_compuesto += capital * 0.05
    meses += 1

print(f'Meses: {meses}')
