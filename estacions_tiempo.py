# Las cuatro estaciones del año

tiempo = int(input('Numero del mes actual (1, 12): '))

if tiempo in (1, 2, 3):
    print('Winter')
elif tiempo in (4, 5, 6):
    print('Spring')
elif tiempo in (7, 8, 9):
    print('Summer')
elif tiempo in (10, 11, 12):
    print('Autumn')
else:
    print('Invalid')
