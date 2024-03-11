#El sombrero seleccionador

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('El sombrero Seleccionador!')
print('Este Sombrero decidira segun tus respuestas en que casa vas.')
print('')
print('🦁Gryffindor')
print('🦅Ravenclaw')
print('🦡Hufflepuff')
print('🐍Slytherin')
print('')

print('Q1) ¿Te gusta el amanecer o el anochecer?')
print('   1) Amanecer')
print('   2) Anochecer')
print('')
q1 = int(input(''))
print('')

print('Q2) Cuando esté muerto, quiero que la gente me recuerde como')
print('   1) El Bueno')
print('   2) El Grande')
print('   3) El Sabio')    
print('   4) El Atrevido')
print('')
q2 = int(input(''))
print('')    

print('Q3) Que tipo de instrumento te gusta mas?')
print('   1) El violin')    
print('   2) La trompeta')    
print('   3) El piano')    
print('   4) El tambor')
print('')    
q3 = int(input(''))
print('')

if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Entrada incorrecta.')

if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print('Entrada incorrecta')

if q3 == 1:
    Slytherin += 4
elif q3 == 2:
    Hufflepuff += 4
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4
else:
    print('Entrada incorrecta')    

if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
    print('Bienvenido a Gryffindor🦁!')
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
    print('Bienvenido a Slytherin🐍!')
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print('Bienvenido a Hufflepuff🦡!')
elif Ravenclaw > Slytherin and Ravenclaw > Hufflepuff and Ravenclaw > Gryffindor:
    print('Bienvenido a Ravenclaw🦅!')
else:
    print('No mereces ninguna casa...')


print('')