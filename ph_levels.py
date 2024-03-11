#Calcular el pH

ph = int(input('What is the value?(0, 14) '))

if ph > 7:
    print('Baisc')
elif ph < 7:
    print('Acidic')
else:
    print('Neutral')