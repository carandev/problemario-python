cheque = int(input('Ingresa el valor del cheque: '))

while cheque != 0: 
    num_diez = 0
    num_dos = 0
    num_cien = 0

    if cheque > 10_000:
        while cheque >= 10_000:
            cheque -= 10_000
            num_diez += 1
            
        print(cheque)
    if cheque > 2_000:
        while cheque >= 2_000:
            cheque -= 2_000
            num_dos += 1

    if cheque > 100:
        while cheque >= 100:
            cheque -= 100
            num_cien += 1

    print(f'Se entregan {num_diez} billetes de $10.000')
    print(f'Se entregan {num_dos} billetes de $2.000')
    print(f'Se entregan {num_cien} billetes de $100')

    cheque = int(input('Ingresa el valor del siguiente cheque: '))
    
