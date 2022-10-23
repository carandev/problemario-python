year = 1980
habitantes_a = 3_500_000
crecimiento_a = 0.07
habitantes_b = 5_000_000
crecimiento_b = 0.05

while habitantes_a < habitantes_b:
    year += 1
    habitantes_a += habitantes_a * crecimiento_a
    habitantes_b += habitantes_b * crecimiento_b

print(f'La población de la ciudad A es mayor en el año {year}')
