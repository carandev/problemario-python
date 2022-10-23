numero_cedula = input("Número de cédula: ")
salario_bruto = float(input("Salario bruto: "))
descuento = salario_bruto * 0.05

if salario_bruto > 500_000:
    descuento = salario_bruto * 0.1

salario_neto = salario_bruto - descuento

print(f'Cédula: {numero_cedula}')
print(f'Salario bruto: {salario_bruto}')
print(f'Descuento: {descuento}')
print(f'Salario neto: {salario_neto}')
