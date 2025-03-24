import numpy as np
import random


size = int(input('Ingrese el largo del pasillo: '))

cuadro = '[ ]'

matriz = np.array([[cuadro] * size for _ in range(11)])
matriz[5][0] = '[S]'

posactual = [5,0]

def randcoord():
    x = random.randrange(0,size)
    y = random.randrange(0,11)
    lista = [x,y]
    return lista
    
def generarfin():
    i = 1
    x = size - 1
    while i != 0:
        y = randcoord()[1]

        if matriz[y][x] == '[ ]':
            matriz[y][x] = '[*]'
            i -= 1
        else:
            y = randcoord()[1]

generarfin()

def mostrar_tablero():
    for fila in matriz:
        print(" ".join(map(str, fila)))

def genguard(cant_guardias):
    while cant_guardias != 0:
        x = randcoord()[0]
        y = randcoord()[1]

        if matriz[y][x] == '[ ]':
            matriz[y][x] = '[!]'
            cant_guardias -= 1
        else:
            x = randcoord()[0]
            y = randcoord()[1]
    mostrar_tablero()

guardias = int(input('Ingrese cantidad de guardias: '))
genguard(guardias)

def generarnumero():
    if size > 100:
        hack = random.randint(0,500)
        base = 2
    elif 20 <= size <= 100:
        hack = random.randint(0,100)
        base = 1
    elif size < 20:
        hack = random.randint(0,20)
        base = 0
        
    lista = [hack, base]
    return lista

hack = generarnumero()[0]
base = generarnumero()[1]

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
    
    for numero in hexadecimal:
        if numero not in hexnumbers:
            print('Ingresa un numero Hexadecimal correcto')
            return
    
    i = 0
    for number in revert:
        number = hexnumbers.index(number)
        total += number*(16**i)
        i += 1
        
    return total
    
def bintodec(input):
    binumbers= ['0','1']
    
    for numero in input:
        if numero not in binumbers:
            print('Ingresa un numero Binario correcto')
            return
    
    numstr = str(input)[::-1]
    i = 0
    dec = 0
    for c in numstr:
        c = int(c)
        dec += c*(2**i)
        i += 1
    return dec

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

def octtodec(input):
    octalnumbers = ['0','1','2','3','4','5','6','7']
    
    for numero in input:
        if numero not in octalnumbers:
            print('Ingresa un numero Octal correcto')
            return
    
    
    numstr = str(input)[::-1]
    i = 0
    dec = 0
    for c in numstr:
        c = int(c)
        dec += c*(8**i)
        i += 1
    return dec

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

def ganar():
    if base == 0:
        print('decifra el siguiente numero: ', ''.join(map(str,dectobin(hack))))
    elif base == 1:
        print('decifra el siguiente numero: ', ''.join(map(str,dectooct(hack))))
    elif base == 2:
        print('decifra el siguiente numero: ', ''.join(map(str,dectohexa(hack))))

    respuesta = int(input('-->'))
    
    if respuesta == hack:
        print('YOU WIN MF')
        return
    else:
        print('Aber estudiao')
        return

def verificar(posiciones):
    if matriz[posiciones[0]][posiciones[1]] == '[ ]':
        return True
    elif matriz[posiciones[0]][posiciones[1]] == '[!]':
        print('Atrapao')
        return False
    elif matriz[posiciones[0]][posiciones[1]] == '[*]':
        ganar()
        return False

def movement(direccion, espacios):
    if direccion == 'w':
        spaces = espacios
        if posactual[0] - espacios >= 0:
            matriz[posactual[0]][posactual[1]] = '[ ]'
            while spaces != 0:
                posactual[0] -= 1
                if verificar(posactual):
                    spaces -= 1
                else:
                    return 0
            matriz[posactual[0]][posactual[1]] = '[S]'
            return 1
        else:
            print('Ingrese una casilla posible.')
            return 1
        
    elif direccion == 's':
        spaces = espacios
        if posactual[0] + espacios <= 10: 
            matriz[posactual[0]][posactual[1]] = '[ ]'
            while spaces != 0:
                posactual[0] += 1
                if verificar(posactual):
                    spaces -= 1
                else:
                    return 0
            matriz[posactual[0]][posactual[1]] = '[S]'
            return 1
        else:
            print('Ingrese una casilla posible.')
            return 1
            
    elif direccion == 'a':
        spaces = espacios
        if posactual[1] - espacios >= 0: 
            matriz[posactual[0]][posactual[1]] = '[ ]'
            while spaces != 0:
                posactual[1] -= 1
                if verificar(posactual):
                    spaces -= 1
                else:
                    return 0
            matriz[posactual[0]][posactual[1]] = '[S]'
            return 1
        else:
            print('Ingrese una casilla posible.')
            return 1
        
    elif direccion == 'd':
        spaces = espacios
        if posactual[1] + espacios <= size-1:
            matriz[posactual[0]][posactual[1]] = '[ ]'
            while spaces != 0:
                posactual[1] += 1
                if verificar(posactual):
                    spaces -= 1
                else:
                    return 0
            matriz[posactual[0]][posactual[1]] = '[S]'
            return 1
        else:
            print('Ingrese una casilla posible.')
            return 1
 
flag = 1

while flag:
    movimientos = ['w','s','a','d','-1']
    
    movimiento = input('''Ingresa una accion:
                       w: Moverse hacia arriba.
                       s: Moverse hacia abajo.
                       d: Moverse hacia la derecha.
                       a: Moverse hacia la izquierda.
                       -1: salir.
                       ''')
    
    if movimiento not in movimientos:
        print('Ingrese un movimiento valido')
        continue
    
    if movimiento == '-1':
        break
    
    if base == 0:
        espacios = input('Escriba cuantas casillas se quiere mover en binario: ')
        espacios = bintodec(espacios)
        flag = movement(movimiento,espacios)
        if flag:
            mostrar_tablero()
    
    elif base == 1:
        espacios = input('Escriba cuantas casillas se quiere mover en octal: ')
        espacios = octtodec(espacios)
        flag = movement(movimiento,espacios)
        if flag:
            mostrar_tablero()
    
    elif base == 2:
        espacios = input('Escriba cuantas casillas se quiere mover en Hexadecimal: ')
        espacios = hexatodec(espacios)
        flag = movement(movimiento,espacios)
        if flag:
            mostrar_tablero()