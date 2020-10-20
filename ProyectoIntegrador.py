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
    

    Parameters Despliega un menu para entrar a los menus de los datos nacionales, y los datos por estado.
               Tambien tiene la opcion de salir.
    ----------
    archivo : str
        Archivos de casos de Covid.

    Returns
    -------
    None.

    """
    
    archivo = open(archivo,"r")

    print("1: Mostrar Datos Nacionales")
    print("2: Mostrar Datos De Un Estado")
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
    
    """
    

    Parameters Despliega los datos de los casos de covid nacionales, y tambien regresa al menu principal. 
               Las opciones a elegir son: 
                   1: Revisar casos por día
                   2: Ver todos los casos
                   3: Ver grafica de todos los casos por mes
                   4: Ver grafica de todos los casos
                   5: Regresar
    ----------
    archivo : str
        Archivos de casos de Covid.

    Returns
    -------
    None.

    """
    
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
        print("Elije un mes: ")
        print("1: Marzo")
        print("2: Abril")
        print("3: Mayo")
        print("4: Junio")
        print("5: Julio")
        mes = int(input())
        
        print("Elije un dia: ")
        for i in range(meses[mes][2]):
            print(f"{i}: dia {meses[mes][3][i][0:2]}")
        dia = int(input())
        
        casos = int(meses[mes][4][dia])
        dia = int(meses[mes][3][dia][0:2])
        print(f"El numero de casos en el dia {dia} es de {casos}")
        
        print("1: Regresar al menu")
        tecla = int(input())
        if tecla == 1:
            print(menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv'))
            
    elif tecla == 2:
        casos_totales = 0
        rango = len(matriz[longuitud_matriz-1][3:])
        for i in range(3,rango):
            casos_totales = casos_totales + int(matriz[longuitud_matriz-1][i])
        print(f"Los casos totales son de: {casos_totales}")
        
        print("1: Regresar al menu")
        tecla = int(input())
        if tecla == 1:
            print(menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv'))
            
    elif tecla == 3:
        print("Elija un mes: ")
        print("1: Marzo")
        print("2: Abril")
        print("3: Mayo")
        print("4: Junio")
        print("5: Julio")
        tecla = int(input())
    
        
        mes = meses[tecla][0]
        numero_dias = meses[tecla][2]
        casos = meses[tecla][4]
        for i in range(len(casos)):
            casos[i] = int(casos[i])
        cantidad_dias = []
        for i in range(1,numero_dias+1):
            cantidad_dias.append(i)
            
        print(grafica_mesesN(mes,cantidad_dias,casos))
        
    elif tecla == 4:
        nombre_meses = []
        for i in range(1,len(meses)+1):
            nombre_meses.append(meses[i][0])
            
        casos_mes = []
        suma = 0
        for i in range(1,len(meses)+1):
            for j in range(meses[i][2]):
                suma = suma +int(meses[i][4][j])
            casos_mes.append(suma)
            suma = 0
            
        print(grafica_total(nombre_meses,casos_mes))
        
    elif tecla == 5:
        print(menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv'))
        
def menu_de_estados(archivo):
    """
    

    Parameters Despliega los datos de los casos de covid por estados, y tambien regresa al menu principal. 
               Las opciones a elegir son: 
                   1: Revisar casos por día
                   2: Ver todos los casos
                   3: Ver grafica de todos los casos por mes
                   4: Ver grafica de todos los casos
                   5: Regresar
    ----------
    archivo : str
        Archivos de casos de Covid.

    Returns
    -------
    None.

    """
    
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
            print("Elije un mes: ")
            print("1: Marzo")
            print("2: Abril")
            print("3: Mayo")
            print("4: Junio")
            print("5: Julio")
            mes = int(input())
            
            print("Elije un dia: ")
            for i in range(meses[mes][2]):
                print(f"{i}: dia {meses[mes][3][i][0:2]}")
            dia = int(input())
            
            casos = int(meses[mes][4][dia])
            dia = int(meses[mes][3][dia][0:2])
            print(f"El numero de casos en el dia {dia} es de {casos}")
            
            print("1: Regresar al menu")
            tecla = int(input())
            if tecla == 1:
                print(menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv'))
                
        elif tecla == 2:
            casos_totales = 0
            rango = len(matriz[longuitud_matriz-1][3:])
            for i in range(3,rango):
                casos_totales = casos_totales + int(matriz[longuitud_matriz-1][i])
            print(f"Los casos totales son de: {casos_totales}")
            
            print("1: Regresar al menu")
            tecla = int(input())
            if tecla == 1:
                print(menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv'))
                
                
                
        elif tecla == 3:
            print("Elija un mes: ")
            print("1: Marzo")
            print("2: Abril")
            print("3: Mayo")
            print("4: Junio")
            print("5: Julio")
            tecla = int(input())
        
            
            mes = meses[tecla][0]
            numero_dias = meses[tecla][2]
            casos = meses[tecla][4]
            for i in range(len(casos)):
                casos[i] = int(casos[i])
            cantidad_dias = []
            for i in range(1,numero_dias+1):
                cantidad_dias.append(i)
                
            print(grafica_mesesE(mes,cantidad_dias,casos,estados,llave))
            
        elif tecla == 4:
            nombre_meses = []
            for i in range(1,len(meses)+1):
                nombre_meses.append(meses[i][0])
            
            casos_mes = []
            suma = 0
            for i in range(1,len(meses)+1):
                for j in range(meses[i][2]):
                    suma = suma +int(meses[i][4][j])
                casos_mes.append(suma)
                suma = 0
            
            print(grafica_total(nombre_meses,casos_mes))
            
        elif tecla == 5:
            menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv')
            
def grafica_mesesN(mes,cantidad_dias,casos):

    """
    

    Parameters Grafica una grafica de todos los casos por dia en un mes de los datos nacionales.
    ----------
    mes : str
        Mes de la grafica.
    cantidad_dias : list
        Cantidad de dias en el mes.
    casos : list
        Numero de casos por dia.

    Returns
    -------
    None.

    """

    plt.title(f"Casos Covid en el mes de {mes}")
    plt.xlabel("Dias")
    plt.ylabel("Numero de casos")
    plt.plot(cantidad_dias, casos, color="red")
    
def grafica_mesesE(mes,cantidad_dias,casos,estados,llave):
    
    """
    

    Parameters Grafica una grafica de casos por dias por mes de los datos por estado.
    ----------
    mes : str
        Mes de los casos.
    cantidad_dias : list
        Cantidad de dias que hay en el mes.
    casos : list
        Cantidad de casos confirmados por dia.
    estados : dict
        Estados que hay en Mexico.
    llave : int
        Llave para acceder a los estados.

    Returns
    -------
    None.

    """

    plt.title(f"Casos Covid en el mes de {mes} de {estados[llave][2]}")
    plt.xlabel("Dias")
    plt.ylabel("Numero de casos")
    plt.plot(cantidad_dias, casos, color="red")
    
def grafica_total(nombre_meses,casos):

    """
    

    Parameters Grafica una grafica de todos los casos por mes.
    ----------
    nombre_meses : list
        Nombre de los meses.
    casos : list
        Numero de casos por mes.

    Returns
    -------
    None.

    """
    plt.bar(nombre_meses,casos)
    
#Se llama a menu y se le pasa el archivo de casos diarios confirmados de Covid.
menu('Covid19_Casos_Diarios_Estado_Nacional_Confirmados_20200730.csv')
