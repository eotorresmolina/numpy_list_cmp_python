#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"

import numpy as np
import random
import math


def ej1():
    print('\nComenzamos a divertirnos!\n\n')

    '''
    Empecemos a jugar con las listas y su métodos, el objetivo
    es realizar el código lo más simple, ordenado y limpio posible,
    no utilizar bucles donde no haga falta, no "re inventar" una función
    que ya dispongamos de Python. El objetivo es:

    1) Generar una lista 3 numéros aleatorios con random (pueden repetirse),
       que estén comprendidos entre 1 y 10 inclusive
       (NOTA: utilizar comprension de listas a pesar de poder hacerlo
        con un método de la librería random)
    2) Luego de generar la lista sumar los números y ver si el resultado
       de la suma es menor o igual a 21
       a) Si el número es menor o igual a 21 se imprime en pantalla
          la suma y los números recoletados
       b) Si el número es mayor a 21 se debe tirar la lista y volver
          a generar una nueva, repetir este proceso hasta cumplir la
        condicion "a"

    Realizar este proceso iterativo hasta cumplir el objetivo
    '''
    suma = None
    lista_aleatoria = []

    while ((suma is None) or (suma > 21)):
        lista_aleatoria = [random.randrange(1, 11) for num in range(0, 3)]
        print('Lista Aleatoria: {}'.format(lista_aleatoria))
        suma = np.sum(lista_aleatoria)
        if suma <= 21:
            print('Números Recolectados: {}'.format(lista_aleatoria))
            
        print('La Suma de los Números Recolectados es: {}\n'.format(suma))


def ej2():
    print('Comenzamos a ponernos serios!\n')

    '''
    Dado una lista de nombres de personas "nombres" se desea
    obtener una nueva lista filtrada que llamaremos "nombres_filtrados"
    La lista se debe filtrar por comprensión de listas utilizando la
    lista "padron" como parámetro.
    La lista filtrada sodo deberá tener aquellos nombres que empiecen
    con alguna de las letras aceptadas en el "padron".
    '''

    padron = ['A', 'E', 'J', 'T']

    nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

    # Se espera obtener:
    # ['Tamara', 'Juan', 'Alberto'......]
    nombres_filtrados = [nombre for nombre in nombres if (nombre[0] in padron)]
    print('\nLa Lista de Nombres Filtrados es: {}\n\n'.format(nombres_filtrados))


def ej3():
    print("\n\nUn poco de Numpy!\n\n")
    # Ejercicio de funciones
    # Se desea calcular los valores de salida de
    # una función senoidal, dado "X" como el conjunto
    # de valores que deben someter a la función "sin"

    # Conjunto de valores "X" en un array
    x = np.arange(0, 2*np.pi, 0.1)

    # Utilizar la función np.sin para someter cada valor de "X",
    # obtenga el array "y_nump" que tenga los resultados
    # NO utilizar comprensión de listas, solo utilice la
    # funcion de numpy "np.sin"

    # y_nump =
    y_nump = np.sin(x)
    print('Valores de x:\n{}'.format(x))
    print('\n\nValores de Salida de la Función sin de Numpy:\n{}\n'.format(y_nump))

    # Conjunto de valores "X" en una lista
    x = list(np.arange(0, 2*np.pi, 0.1))

    # Utilizar comprensión de listas para obtener la lista
    # "y_list" que tenga todos los valores obtenidos como resultado
    # de someter cada valor de "X" a la función math.sin

    # y_list =
    y_list = [math.sin(num) for num in x]
    print('\nValores de x:\n{}'.format(x))
    print('\n\nValores de Salida de la Función sin de Math:\n{}\n\n'.format(y_list))

    # Este es un ejemplo práctico de cuando es útil usar numpy,
    # basicamente siempre que deseen utilizar una función matemática
    # que esté definida en numpy NO necesitaran un bucle o comprensión
    # de listas para obtener el resultado de un monton de datos a la vez.


def ej4():
    print("\n\nAcercamiento al uso de datos relacionales:\n\n")
    # Transformar variable numéricas en categóricas
    # Se dispone del siguiente diccionario que traduce el número ID
    # de un producto en su nombre, por ejemplo:
    # NOTA: Esta información bien podría ser una tabla SQL: id | producto
    producto = {
                556070: 'Auto',
                704060: 'Moto',
                42135: 'Celular',
                1264: 'Bicicleta',
                905045: 'Computadora',
                }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    # Crear una nueva lista "lista_compra_productos" que transforme la lista
    # de realizada por "ID" de producto en lista por "nombre" producto
    # Iterar sobre la lista "lista_compra_id" para generar la nueva
    # En cada iteración acceder al diccionario para traducir el ID.
    # NOTA: Tener en cuenta que puede haber códigos (IDs) que
    # no esten registrados en el sistema, en esos casos se debe
    # almacenar en la lista la palabra 'NaN', para ello puede hacer uso
    # de condicionales PERO recomendamos leer atentamente el método "get"
    # de diccionarios que tiene un parametro configurable respecto
    # que sucede sino encuentra la "key" en el diccionario.

    lista_compra_productos = [producto.get(id, 'NaN') for id in lista_compra_id]
    print('\nLa Nueva Lista Transformada de "ID" al "Producto" es: {}\n\n'.format(lista_compra_productos))


def ej5():
    print("\n\nAhora sí! buena suerte :)\n\n")

    '''
    Black jack! [o algo parecido :)]

    El objetivo es realizar una aproximación al juego de black jack,
    el objetivo es generar una lista de 2 números aleatorios
    entre 1 al 10 inclusive, y mostrar los "números" al usuario.
    El usuario debe indicar al sistema si desea sacar más
    números para sumarlo a la lista o no sacar más
    A medida que el usuario vaya sacando números aleatorios que se suman
    a su lista se debe ir mostrando en pantalla la suma total
    de los números hasta el momento.
    Cuando el usuario no desee sacar más números o cuando el usuario
    haya superado los 21 (como la suma de todos) se termina la jugada
    y se presenta el resultado en pantalla

    BONUS Track: Realizar las modificaciones necesarias para que jueguen
    dos jugadores y compitan para ver quien sacá la suma de números
    más cercanos a 21 sin pasarse!
    '''

    # Inicialización de Variables:
    suma_j1 = 0
    suma_j2 = 0
    contador = 0
    sacar_numero = True
    sacar_numero_j2 = True
    turno_jugador1 = True
    turno_jugador2 = False

    mano_jugador1 = [random.randint(1, 10) for valor in range(2)]
    suma_j1 = sum(mano_jugador1)
    print('Los Valores de las Cartas del Jugador 1 es: {}'.format(mano_jugador1))
    print('La Suma de los Valores de las Cartas Hasta el Momento: {}\n\n'.format(suma_j1))

    mano_jugador2 = [random.randint(1, 10) for valor in range(2)]
    suma_j2 = sum(mano_jugador2)
    print('Los Valores de las Cartas del Jugador 2 es: {}'.format(mano_jugador2))
    print('La Suma de los Valores de las Cartas Hasta el Momento: {}\n\n'.format(suma_j2))

    while (((suma_j1 <= 21) and (suma_j2 <= 21)) and (sacar_numero is True)):
        if turno_jugador1 is True:
            sacar_numero_j1 = str(input('Jugador 1: ¿Desea sacar Otro Número? [Y/N]: '))
            if sacar_numero_j1.upper( ) in 'YES':
                mano_jugador1.append(random.randint(1, 10))
                sacar_numero_j1 = True
                suma_j1 = sum(mano_jugador1)
            elif sacar_numero_j1.upper( ) in 'NO':
                sacar_numero_j1 = False
                contador = 0
                contador += 1

            print('Los Valores de Carta del Jugador 1 es: {}'.format(mano_jugador1))
            print('La Suma de los Valores Hasta el Momento: {}\n\n'.format(suma_j1))
            turno_jugador1 = False
            turno_jugador2 = True
        
        elif turno_jugador2 is True:
            sacar_numero_j2 = str(input('Jugador 2: ¿Desea sacar Otro Número? [Y/N]: '))
            if sacar_numero_j2.upper( ) in 'YES':
                mano_jugador2.append(random.randint(1, 10))
                sacar_numero_j2 = True
                suma_j2 = sum(mano_jugador2)
            elif sacar_numero_j2.upper( ) in 'NO':
                sacar_numero_j2 = False
                contador += 1

            print('Los Valores de Carta del Jugador 2 es: {}'.format(mano_jugador2))
            print('La Suma de los Valores Hasta el Momento: {}\n\n'.format(suma_j2))
            turno_jugador2 = False
            turno_jugador1 = True

        if contador == 2:
            sacar_numero = sacar_numero_j1 or sacar_numero_j2


    if suma_j1 > suma_j2:
        if suma_j1 == 21:
            print('\nEl Jugador 1 Ganó!! Hizo BlackJack!!\n\n')
        elif suma_j1 < 21:
            print('\nEl Jugador 1 Ganó!!\n\n')
        else:
            if suma_j2 < 21:
                print('\nEl Jugador 2 Ganó!!\n\n')
            elif suma_j2 == 21:
                print('\nEl Jugador 2 Ganó!! Hizo BlackJack!!\n\n')
            else:
                print('\nAmbos Jugadores Pierden!! La Casa Gana!\n\n')
    elif suma_j1 == suma_j2:
        if suma_j1 == 21:
            print('\nLos Jugadores Hicieron BlackJack!! Es un Empate.\n\n')
        elif suma_j1 > 21:
            print('\nAmbos Jugadores Pierden!! La Casa Gana!\n\n')
        else:
            print('\nLos Jugadores Empataron!!\n\n')
    else:
        if suma_j2 == 21:
            print('\nEl Jugador 2 Ganó!! Hizo BlackJack!!\n\n')
        elif suma_j2 < 21:
            print('\nEl Jugador 2 Ganó!!\n\n')
        else:
            if suma_j1 < 21:
                print('\nEl Jugador 1 Ganó!!\n\n')
            elif suma_j1 == 21:
                print('\nEl Jugador 1 Ganó!! Hizo BlackJack!!\n\n')
            else:
                print('\nAmbos Jugadores Pierden!! La Casa Gana!\n\n')



if __name__ == '__main__':
    print("\n\nEjercicios de práctica:\n\n")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
