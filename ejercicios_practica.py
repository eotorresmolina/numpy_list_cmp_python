#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.2"

import numpy as np
import math
import random
from random import randrange


def ej1():
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)

    numero = float(input('\n\nIngrese un Número: '))
    potencia_2 = lambda x: x**2
    potencia_numero = potencia_2(numero)
    print('\nLa Potencia de 2 del Número Ingresado es: {}\n\n'.format(potencia_numero))

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    # numeros_potencia = list(map....)
    numeros_potencia = list(map(lambda x: x**2, numeros))
    print('Lista Original: {}'.format(numeros))
    print('La Lista de Números Elevados al Cuadrado: {}\n\n'.format(numeros_potencia))


def ej2():
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro

    string = str(input('\n\nIngrese una Cadena de Caracteres: '))

    # len_string = lambda......
    len_string = (lambda x: len(x))(string)
    print('La Cadena de Caracteres que Ingresó posee {} Caracteres.\n\n'.format(len_string))

    # 2)
    # Lista de string
    palabras = ['Inove', 'casa', 'programacion']

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "len_string" dentro del map, debe colocar
    # directamente la lambda.

    # palabras_len = list(map....)
    palabras_len = list(map(lambda x: len(x), palabras))
    print('Lista Original: {}'.format(palabras))
    print('El Tamaño de Cada elemento de la Lista Original es: {}\n\n'.format(palabras_len))



def ej3():
    # Práctica de comprensión de listas
    # 1)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá tener un tamaño de 11
    # números, conteniendo del 0 al 10 inclusive

    # lista_0_10 = [......]
    lista_0_10 = [numero for numero in range(0, 11)]        # Compresión de Listas.
    print('\n\nLa Lista Generada es: {}\n\n'.format(lista_0_10))

    # 2)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener la tabla del 5,
    # desde el múltiplo 0 al múltiplo 10
    # El resultado esperado es:
    # [0 5 10 15 20 25 30 35 40 45 50]
    # Utilizar comprensión de listas para generar essa lista
    # Lo esperable es que realicen una lista de 11 elementos,
    # del 0 al 10 (como el ejer anterior) pero que cada
    # elemento lo multipliquen x5.

    # tabla_5 = [......]
    tabla_5 = [(numero * 5) for numero in range(0, 11)]
    print('\n\nLa Lista Generada es: {}\n\n'.format(tabla_5))


    # 3)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse).
    # NOTA: Importar le módulo random y utiliza randrange
    # o randint para generar números aleatorios.
    # https://docs.python.org/3/library/random.html

    # dias_mes = [.....]
    dias_mes = [randrange(1,31,1) for dia in range(0, 11) ]
    print('La Lista Generada es: {}\n\n'.format(dias_mes))


def ej4():
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']
    conv_str_int = [(int(elemento) if (elemento.isdigit( ) is True) else 0) for elemento in list_numeros_str]
    print('\n\nLista Original: {}'.format(list_numeros_str))
    print('La Lista Original Convertida a una Lista de Números es: {}\n\n'.format(conv_str_int))

    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?    

    list_numeros_str = ['-5', '2', '-3', '', '7', 'NaN']  
    conv_str_int = [(int(elemento) if (elemento.isdigit( ) is True) else 0) for elemento in list_numeros_str]
    print('Lista Original: {}'.format(list_numeros_str))
    print('La Lista Original Convertida a una Lista de Números es: {}'.format(conv_str_int))
    print('Se Observa que Si se Hace Negativo un Número de la Lista Original, el método "isdigit( )" no la Toma como un Número.\n\n')


def ej5():
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # La lista accesos contiene los números de ID de personal
    # que ingresaron por ese molinete

    # 1)
    # Generar una lista por comprensión de la lista "accesos"
    # una lista que solo contenga (filtrado) los ID de personal
    # entre 1 al 10 inclusive, se desea separar del grupo de accesos
    # los ID entre el 1 y 10.
    # De la lista resultante informar cuantas personas/personal
    # comprendido en dicho rango pasó por ese molinete

    # personal_1_10 = [.....]
    personal_1_10 = [id for id in accesos if (1 <= id <= 10)]
    print('\n\nLa Lista de Accesos de Personal es: {}'.format(accesos))
    print('La Lista Filtrada es: {}'.format(personal_1_10))
    print('La Cantidad de Personal que Ingresó por ese Molinete es de: {} Personas.\n\n'.format(len(personal_1_10)))

    # 2)
    # Generar una lista por comprensión de la listas "accesos"
    # cuyo ID de personal esté dentro de los ID válidos para ingresar
    # por ese molinete:
    id_validos = [3, 4, 7, 8, 15]
    # Debe generar una nueva lista basada en "accesos" filtrada por los ID
    # aprobados en "id_validos".
    # TIP: Utilizar el operador "in" para chequear si un ID de accesos está
    # dentro de "id_validos"

    # personal_valido = [.....]
    personal_valido = [id for id in accesos if (id in id_validos)]
    print('La Lista de ID Válidos es: {}\n\n'.format(personal_valido))


def ej6():
    # Ejercicio de funciones Numpy
    # Arme un array con el método np.arange
    # el cual este acotado entre 0 y 1000
    # De dicho array calcular las siguientes operaciones:

    # 1)
    # Calcular la suma de todos los elementos en el array
    # utilizar el método "sum" de numpy

    # suma = ....
    array_int = np.arange(0, 1000)
    print('\n\nLa Lista de Números es:\n{}'.format(array_int))
    suma = np.sum(array_int)
    print('\nLa Suma de los Números de la Lista es: {}\n\n'.format(suma))

    # 2)
    # Calcular la diferencia de todos los elementos en el array
    # utilizar el método "diff" de numpy

    # diferencia = ....
    diferencia = np.diff(array_int)
    print('La Diferencia de los Números de la Lista es:\n{}\n\n'.format(diferencia))

    # 3)
    # Utilizar la funcion "where" para reemplazar los números múltiplos
    # de "5" por un "0"
    # Ojo: ¿Que operador matemático utilizará para saber si un número es
    # múltiplo de "5"? Ese operador ya lo conoce y lo viene utilizando
    # bastante para saber si un número es múltiplo de "2"

    # nuevo_array = ....
    nuevo_array = np.where((array_int % 5) != 0, array_int, 0) 
    print('La Nueva Lista con los Números que Son Múltiplos de 5 es:\n{}\n\n'.format(nuevo_array))


if __name__ == '__main__':
    print("\n\nBienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
    ej6()
