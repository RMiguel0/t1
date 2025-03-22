import numpy as np
import random


size = int(input('Ingrese el largo del pasillo: '))

cuadro = '[ ]'

matriz = np.array([[cuadro] * size for _ in range(11)])
matriz[5][0] = '[S]'

for fila in matriz:
    print(" ".join(map(str, fila)))


def generarnumero():
    if size >= 100:
        hack = random.randint(0,500)
    elif 20 <= size < 100:
        hack = random.randint(0,100)
    elif size < 20:
        hack = random.randint(0,20)
    
    return hack

hack = generarnumero()

print('hack =', hack)

def resto16(numero, lista=None):
    if lista is None:
        lista = []
    
    resto = numero % 16
    lista.append(resto)
    
    new = numero // 16
    
    if new == 0:
        return lista
    else:
        return resto16(new, lista)



def dectohexa(numhack):
    hexnumbers = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    result = []
    
    if numhack < 16:
        return hexnumbers[numhack]
    else:
        result = resto16(numhack)
    
    i = 0
    for num in result:
        result[i] = hexnumbers[num]
        i += 1
        
    result.reverse()
    return result

def hexatodec(hexadecimal):
    revert = str(hexadecimal)[::-1]
    hexnumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    total = 0
    
    i = 0
    for number in revert:
        number = hexnumbers.index(number)
        total += number*(16**i)
        i += 1
        
    return total
    
def bintodec(input):
    numstr = str(input)[::-1]
    i = 0
    dec = 0
    for c in numstr:
        c = int(c)
        dec += c*(2**i)
        i += 1
    return dec

def octtodec(input):
    numstr = str(input)[::-1]
    i = 0
    dec = 0
    for c in numstr:
        c = int(c)
        dec += c*(8**i)
        i += 1
    return dec

def resto2(numero, lista=None):
    if lista is None:
        lista = []
    
    resto = numero % 2
    lista.append(resto)
    
    new = numero // 2
    
    if new == 0:
        return lista
    else:
        return resto2(new, lista)
    
def dectobin(numhack):
    binnumbers = [0,1]
    result = []
    
    if numhack < 2:
        return binnumbers[numhack]
    else:
        result = resto2(numhack)
    
    i = 0
    for num in result:
        result[i] = binnumbers[num]
        i += 1
        
    result.reverse()
    return result

def dectooct(numhack):
    octnumbers = [0,1,2,3,4,5,6,7]
    result = []
    
    if numhack < 2:
        return octnumbers[numhack]
    else:
        result = resto8(numhack)
    
    i = 0
    for num in result:
        result[i] = octnumbers[num]
        i += 1
        
    result.reverse()
    return result

def resto8(numero, lista=None):
    if lista is None:
        lista = []
    
    resto = numero % 8
    lista.append(resto)
    
    new = numero // 8
    
    if new == 0:
        return lista
    else:
        return resto8(new, lista)
print(dectooct(347))



