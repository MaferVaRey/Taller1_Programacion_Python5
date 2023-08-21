di1 = int(input('Ingrese el dividendo: '))
di2 = int(input('Ingrese el divisor: '))

division = di1 / di2
modulo = di1 % di2

print('División: ', division)
print('Residuo: ', modulo)

if modulo == 0:
    print('La división es exacta')
else:
    print('La división NO es exacta')
