# VERSION 2
import re

binPattern = r'^[0-1]+$'
decPattern = r'^[0-9]+$'
hexPattern = r'^([0-9]|[A-F])+$'
octPattern = r'^[0-9]*[0-7]+$'

types = {
    '1': 'Decimal',
    '2': 'Binario',
    '3': 'Hexadecimal',
    '4': 'Octal'
}

patternMap = {
    '1': decPattern,
    '2': binPattern,
    '3': hexPattern,
    '4': octPattern
}


def validateNumberType(type, number):
    return re.match(patternMap[type], number)


def validateType(type):
    if types[type]:
        return True
    else:
        print('El valor ingresado no es parte de las opciones disponibles, verifique e ingrese nuevamente')
        return False


def getType():
    return input('1. Decimal\n2. Binario\n3. Hexadecimal\n4. Octal\n')


def convert(number, origin, dest):
    if origin == dest:
        return number
    elif origin == '1':
        if dest == '2':
            return decToBase(number, 2)
        if dest == '3':
            return decToBase(number, 16)
        if dest == '4':
            return decToBase(number, 8)
    elif origin == '2':
        if dest == '1':
            return baseToDec(number, 2)
        if dest == '3':
            number = str(convert(number, origin, '1'))
            return convert(number, '1', '3')
        if dest == '4':
            number = str(convert(number, origin, '1'))
            return convert(number, '1', '4')
    elif origin == '3':
        if dest == '1':
            return baseToDec(number, 16)
        if dest == '2':
            number = str(convert(number, origin, '1'))
            return convert(number, '1', '2')
        if dest == '4':
            number = str(convert(number, origin, '1'))
            return convert(number, '1', '4')
    elif origin == '4':
        if dest == '1':
            return baseToDec(number, 8)
        if dest == '2':
            number = str(convert(number, origin, '1'))
            return convert(number, '1', '2')
        if dest == '3':
            number = str(convert(number, origin, '1'))
            return convert(number, '1', '3')


def decToBase(number, base):
    parsedNumber = int(number)
    result = ''

    while parsedNumber > 0:
        mod = int(parsedNumber % base)
        if base == 16:
            mod = getHexValue(mod)
        parsedNumber = int(parsedNumber / base)
        result = str(mod) + result

    return result


def baseToDec(number, base):
    position = 0
    result = 0
    binary = number[::-1]

    for n in binary:
        value = base**position
        if base == 16:
            n = getDecValue(n)
        result += value*int(n)
        position += 1

    return result


def getHexValue(value):
    values = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }

    value = str(value)

    if value in values:
        return values[value]
    else:
        return value


def getDecValue(value):
    values = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
    }

    value = str(value)

    if value in values:
        return values[value]
    else:
        return value


def showOptions():
    print('Seleccione un tipo de dato para ingresar:')
    originType = getType()
    if validateType(originType):
        number = input(
            'Ingrese el número a convertir (' + types[originType] + '): ').upper()
        if validateNumberType(originType, number):
            print('Seleccione un tipo de dato para ingresar:')
            destType = getType()
            if validateType(originType):
                print('Convirtiendo')
                result = convert(number, originType, destType)
                print('Resultado:')
                print(result)
            else:
                showOptions()
        else:
            print('Error: El número ' + number + ' no es del tipo seleccionado (' +
                  types[originType] + ') o es un valor vacío')
    else:
        showOptions()


print('Conversor de Bases')
showOptions()
