# Calculadora de peso en cada planeta del sistema solar

print('Número	Planeta	    Gravedad relativa')
print('1	    Mercurio	0,38')
print('2	    Venus	    0,91')
print('3	    Marte	    0,38')
print('4	    Júpiter	    2.53')
print('5	    Saturno	    1.07')
print('6	    Urano	    0,89')
print('7	    Neptuno	    1.14')

earth_weight = float(input('Enter your weight: '))
planet = int(input('Enter the planet number: '))

if planet == 1:
    destination_weight = earth_weight * 0.38
elif planet == 2:
    destination_weight = earth_weight * 0.91
elif planet == 3:
    destination_weight = earth_weight * 0.38
elif planet == 4:
    destination_weight = earth_weight * 2.53
elif planet == 5:
    destination_weight = earth_weight * 1.07
elif planet == 6:
    destination_weight = earth_weight * 0.89
elif planet == 7:
    destination_weight = earth_weight * 1.14
else:
    print('Invalid planet number')

print(destination_weight)
