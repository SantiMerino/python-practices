# Programando nuestro primer juego:
import random

aleatorio = random.randint(1, 100)
cant = int(input('Ingresa la cantidad de intentos: '))
won = False
contador = 0
# print(aleatorio)
guess = ''

for i in range(cant):
    print('---------------------------------------------------------')
    guess = int(input('Intenta adivinar el número del 1 al 100: '))
    if guess == aleatorio:
        won = True
        break
    elif guess != aleatorio:
        contador = contador+1
        if contador == cant:
            print('te quedaste sin intentos')
            break
        elif guess > aleatorio:
            print('te fuiste muy alto')
        elif guess < aleatorio:
            print('te fuiste muy bajo')
        # print(contador)
        print('vuelve a intentarlo')

if won == True: 
    print('Ganaste')


