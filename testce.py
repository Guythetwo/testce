number1 = 0
number2 = 0
ifwhat = ''

while True:
    in_number1 = input('What number_1 or Reset: ')
    if in_number1 == 'Reset' or in_number1 == 'reset':
        number1 = 0
        number2 = 0
        ifwhat = ''
        continue
    in_ifwhat = input('+,-,*,/ or Reset: ')
    if in_ifwhat == 'Reset' or in_ifwhat == 'reset':
        number1 = 0
        number2 = 0
        ifwhat = ''
        continue
    in_number2 = input('What number_2 or Reset: ')
    if in_number2 == 'Reset' or in_number2 == 'reset':
        number1 = 0
        number2 = 0
        ifwhat = ''
        continue
    number1 = int(in_number1)
    number2 = int(in_number2)
    ifwhat = in_ifwhat
    if in_ifwhat == '+':
        print(str(number1),str(ifwhat),str(number2),end=(' = '))
        print(number1 + number2)
        number1 = 0
        number2 = 0
        ifwhat = ''
    elif in_ifwhat == '-':
        print(str(number1),str(ifwhat),str(number2),end=(' = '))
        print(number1 - number2)
        number1 = 0
        number2 = 0
        ifwhat = ''
    elif in_ifwhat == '*':
        print(str(number1),str(ifwhat),str(number2),end=(' = '))
        print(number1 * number2)
        number1 = 0
        number2 = 0
        ifwhat = ''
    elif in_ifwhat == '/':
        print(str(number1),str(ifwhat),str(number2),end=(' = '))
        print(number1 / number2)
        number1 = 0
        number2 = 0
        ifwhat = ''
    else:
        print('o-o')
        number1 = 0
        number2 = 0
        ifwhat = ''