# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:12:34 2020

@author: Nadia
"""
#Se importa el os
#Se importa el matplotlib.pyplot como plt
import os
import matplotlib.pyplot as plt


def menu(archivo):

    """
    

    Parameters
    ----------
    archivo : str
        Archivos de casos de Covid.

    Returns
    -------
    None.

    """
    
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
        print('Saliendo')
        os.system('cls')
        return
        
def menu_nacional(archivo):
    
    #Matriz de los datos del Archivo Covid
    matriz = []
    for linea in archivo:
        x = linea.split(",")
        matriz.append(x)
    longuitud_matriz = len(matriz)
        
    print(f"La poblacion total es de: {matriz[33][1]}")
    print("1: Revisar casos por día")
    print("2: Ver todos los casos")
    print("3: Ver grafica de todos los casos por mes")
    print("4: Ver grafica de todos los casos")
    print("5: Regresar")
    tecla = int(input())
        
    meses = {1: ["Marzo","03",len(matriz[0][3:30]),matriz[0][3:30],matriz[longuitud_matriz-1][3:30]],
                 2:["Abril","04",len(matriz[0][30:60]),matriz[0][30:60],matriz[longuitud_matriz-1][30:60]], 
                 3: ["Mayo","05",len(matriz[0][60:91]),matriz[0][60:91],matriz[longuitud_matriz-1][60:91]],
                 4: ["Junio","06",len(matriz[0][91:121]),matriz[0][91:121],matriz[longuitud_matriz-1][91:121]], 
                 5: ["Julio","07",len(matriz[0][121:]),matriz[0][121:],matriz[longuitud_matriz-1][121:]]}
    
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
        print("Elija un mes: ")
        print("1: Marzo")
        print("2: Abril")
        print("3: Mayo")
        print("4: Junio")
        print("5: Julio")
        tecla = int(input())
        
        fechas = []
    
        
        mes = meses[tecla][0]
        numero_dias = meses[tecla][2]
        fechas = meses[tecla][3]
        casos = meses[tecla][4]
        for i in range(len(casos)):
            casos[i] = int(casos[i])
        cantidad_dias = []
        for i in range(1,numero_dias+1):
            cantidad_dias.append(i)
            
        print(grafica_mesesN(mes,cantidad_dias,fechas,casos))
        
    elif tecla == 4:
        nombre_meses = []
        for i in range(1,len(meses)+1):
            nombre_meses.append(meses[i][0])
        casos = []
        for i in range(1,len(meses)+1):
            casos.append(max((meses[i][4])))
        for i in range(len(meses)):
            casos[i] = int(casos[i])
        print(grafica_total(nombre_meses,casos))
            
    elif tecla == 5:
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
    
    meses = {1: ["Marzo","03",len(matriz[0][3:30]),matriz[0][3:30],matriz[llave][3:30]],
                 2:["Abril","04",len(matriz[0][30:60]),matriz[0][30:60],matriz[llave][30:60]], 
                 3: ["Mayo","05",len(matriz[0][60:91]),matriz[0][60:91],matriz[llave][60:91]],
                 4: ["Junio","06",len(matriz[0][91:121]),matriz[0][91:121],matriz[llave][91:121]], 
                 5: ["Julio","07",len(matriz[0][121:]),matriz[0][121:],matriz[llave][121:]]}
    
    if llave == 33:
        menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv')
    else:
        print(f"La poblacion total es de: {estados[llave][1]}")
        print("1: Revisar casos por día")
        print("2: Ver todos los casos")
        print("3: Ver grafica de todos los casos por mes")
        print("4: Ver grafica de todos los casos")
        print("5: Regresar")
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
            
            print("Elija un mes: ")
            print("1: Marzo")
            print("2: Abril")
            print("3: Mayo")
            print("4: Junio")
            print("5: Julio")
            tecla = int(input())
            
            fechas = []
        
            
            mes = meses[tecla][0]
            numero_dias = meses[tecla][2]
            fechas = meses[tecla][3]
            casos = meses[tecla][4]
            for i in range(len(casos)):
                casos[i] = int(casos[i])
            cantidad_dias = []
            for i in range(1,numero_dias+1):
                cantidad_dias.append(i)
                
            print(grafica_mesesE(mes,cantidad_dias,fechas,casos,estados,llave))
        elif tecla == 4:
            nombre_meses = []
            for i in range(1,len(meses)+1):
                nombre_meses.append(meses[i][0])
            casos = []
            for i in range(1,len(meses)+1):
                casos.append(max((meses[i][4])))
            for i in range(len(meses)):
                casos[i] = int(casos[i])
            print(grafica_total(nombre_meses,casos))
        elif tecla == 5:
            menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv')
            
def grafica_mesesN(mes,cantidad_dias,fechas,casos):

    plt.title(f"Casos Covid en el mes de {mes}")
    plt.xlabel("Dias")
    plt.ylabel("Numero de casos")
    plt.plot(cantidad_dias, casos, color="red")
    
def grafica_mesesE(mes,cantidad_dias,fechas,casos,estados,llave):

    plt.title(f"Casos Covid en el mes de {mes} de {estados[llave][2]}")
    plt.xlabel("Dias")
    plt.ylabel("Numero de casos")
    plt.plot(cantidad_dias, casos, color="red")
    
def grafica_total(nombre_meses,casos):
    plt.bar(nombre_meses,casos)
    
#Se llama a menu y se le pasa el archivo de casos diarios confirmados de Covid.
menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv')
