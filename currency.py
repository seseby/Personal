# Program that ask the user for the amount they have and calculates in USD

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

pesosD = pesos * 0.00026
solesD = soles * 0.27
reaisD = reais * 0.20

total = pesosD + solesD + reaisD

print(total)