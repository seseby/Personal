# Convertir numeros romanos con PY

final_answer = 0
final_answer1 = 0

numeral_input = input('Entra el numero romano que quieres convertir: ')

def roman_to_int(numeral):
    global final_answer  # Declarar final_answer como global
    if 'CM' in numeral:
        final_answer += 900
        numeral = numeral.replace('CM', '')
    if 'CD' in numeral:
        final_answer += 400
        numeral = numeral.replace('CD', '')
    if 'XC' in numeral:
        final_answer += 90
        numeral = numeral.replace('XC', '')
    if 'XL' in numeral:
        final_answer += 40
        numeral = numeral.replace('XL', '')
    if 'IX' in numeral:
        final_answer += 9
        numeral = numeral.replace('IX', '')
    if 'IV' in numeral:
        final_answer += 4
        numeral = numeral.replace('IV', '')            
    for i in numeral:
        if i == 'M':
            final_answer += 1000
        elif i == 'D':
            final_answer += 500
        elif i == 'C':
            final_answer += 100
        elif i == 'L':
            final_answer += 50
        elif i == 'X': 
            final_answer += 10
        elif i == 'V':
            final_answer += 5
        elif i == 'I':
            final_answer += 1
        
    print('El numero romano que has introducido se convierte a: ' + str(final_answer) + '!')

roman_to_int(numeral_input)

def int_to_roman(numeral):
    final_answer = ''

    if numeral >= 1000:
        final_answer += 'M' * (numeral // 1000)
        numeral %= 1000
    if numeral >= 900:
        final_answer += 'CM'
        numeral -= 900
    if numeral >= 500:
        final_answer += 'D'
        numeral -= 500
    if numeral >= 400:
        final_answer += 'CD'
        numeral -= 400
    if numeral >= 100:
        final_answer += 'C' * (numeral // 100)
        numeral %= 100
    if numeral >= 90:
        final_answer += 'XC'
        numeral -= 90
    if numeral >= 50:
        final_answer += 'L'
        numeral -= 50
    if numeral >= 40:
        final_answer += 'XL'
        numeral -= 40
    if numeral >= 10:
        final_answer += 'X' * (numeral // 10)
        numeral %= 10
    if numeral >= 9:
        final_answer += 'IX'
        numeral -= 9
    if numeral >= 5:
        final_answer += 'V'
        numeral -= 5
    if numeral >= 4:
        final_answer += 'IV'
        numeral -= 4
    if numeral >= 1:
        final_answer += 'I' * numeral

    print('El numero que has introducido se convierte a: ' + final_answer + '!')

numeral_input1 = int(input('Entra el numero que quieres convertir a romano: '))
int_to_roman(numeral_input1)



