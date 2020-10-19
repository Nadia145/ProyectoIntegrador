# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:12:34 2020

@author: Nadia
"""

import os
import matplotlib.pyplot as plt


def menu(archivo):
    
    archivo = open(archivo,"r")
    
    print("1: Mostrar datos Nacionales")
    print("2: Mostrar datos de un Estado")
    print("3: Salir")
    tecla = int(input())
    
    if tecla == 1:
        os.system('cls')
        menu_nacional(archivo)
    elif tecla == 2:
        os.system('cls')
        menu_de_estados(archivo)
    else:
        print('Salir')
        os.system('cls')
        return
        
def menu_nacional(archivo):
    matriz = []
    for linea in archivo:
        x = linea.split(",")
        matriz.append(x)
    longuitud_matriz = len(matriz)
        
    print(f"La poblacion total es de: {matriz[33][1]}")
    print("1: Revisar casos por día")
    print("2: Ver todos los casos")
    print("3: Ver grafica de todos los casos por mes")
    print("4: Regresar")
    tecla = int(input())
        
    if tecla == 1:
        posicion = 0
        print(f"Elije un dia: {matriz[0][3:]}")
        dia = input()
        posicion = matriz[0].index(dia)
        print(f"El numero de casos en el dia {matriz[0][posicion]} es de {matriz[longuitud_matriz-1][posicion]}")
    elif tecla == 2:
        casos_totales = 0
        rango = len(matriz[longuitud_matriz-1][3:])
        for i in range(rango):
            casos_totales = casos_totales + int(matriz[longuitud_matriz-1][i+3])
        print(f"Los casos totales son de: {casos_totales}")
    elif tecla == 3:
        mes = 0
        print("Elija un mes: ")
        print("1: Marzo")
        print("2: Abril")
        print("3: Mayo")
        print("4: Junio")
        print("5: Julio")
        tecla = int(input())
        
        meses = {1: ["Marzo","03",31,matriz[0][3:35]], 2:["Abril","04",30,matriz[0][35:66]], 3: ["Mayo","05",31,matriz[0][66:98]], 4: ["Junio","06",30], 5: ["Julio","07",31]}
        mes = meses[tecla]
            
        
        dias = []
        cantidad_dias = len(matriz[0][3:])
        for i in range(cantidad_dias):
            dias.append(i)
        print(grafica(dias,matriz,meses))
        
    elif tecla == 4:
        print(menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv'))
        
def menu_de_estados(archivo):
    matriz = []
    estados = {}
    for linea in archivo:
        x = linea.split(",")
        matriz.append(x)
    longuitud_matriz = len(matriz)-1
    for i in range(longuitud_matriz):     
        print(f"{i}: {matriz[i][2]}")
    for i in range(1,longuitud_matriz):
        estados[i] = matriz[i] 
    print("33: Salir")
    
    llave = int(input())
    if llave == 33:
        menu()
    else:
        print(f"La poblacion total es de: {estados[llave][1]}")
        print("1: Revisar casos por día")
        print("2: Ver todos los casos")
        print("3: Ver grafica de todos los casos")
        print("4: Regresar")
        tecla = int(input())
        casos_totales = 0
        if tecla == 1:
            print(f"Elije un dia: {matriz[0][3:]}")
            dia = input()
            posicion = matriz[0].index(dia)
            print(f"El numero de casos en el dia {matriz[0][posicion]} es de {estados[llave][posicion]}")
        elif tecla == 2:
            rango = len(matriz[longuitud_matriz][3:])
            for i in range(rango):
                casos_totales = casos_totales + int(matriz[longuitud_matriz][i+3])
            print(f"Los casos totales son de: {casos_totales}")
        elif tecla == 3:
            pass
        elif tecla == 4:
            menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv')
            
def grafica(dias,matriz,mes):
    a = [0, -100, 25, 67, -323]
    b = [0, 3, 7, 3, 9]
    fecha = []
    plt.title(f"Casos Covid en el mes de {mes[0]}")
    plt.xlabel("Dias")
    plt.ylabel("Numero de casos")
    plt.axis([-50, 80, 2, 8])
    fecha.append(matriz[0][3:])
    plt.xticks((dias), (fecha))
    plt.plot(a, b, color="red")
    
    
        
        
menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv')
