altura = float(input('Altura: '))
quinta_parte = altura / 5
altura_rebote = altura
rebote = 0

while altura_rebote > quinta_parte:
    altura_rebote -= altura * 0.1
    rebote += 1

print(f'La pelota no alcanza a subir la quinta parte en el rebote {rebote}')
