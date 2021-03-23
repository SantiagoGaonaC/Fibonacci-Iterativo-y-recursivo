# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:29:29 2021

Autores: 
    SANTIAGO GAONA CARVAJAL
    LUIS DIAZ DIAZ

"""
from timeit import default_timer

def fib(n): #Funcion Fibonacci Iterativo
    terminos = [0,1]
    i = 2
    while i <= n:
        terminos.append(terminos[i-1]+terminos[i-2]) #Fibonacci
        i = i + 1
    return terminos[n]

def fibonacci_recursivo(n): #Fibonacci Recursivo
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) #Fibonacci
    

def suma_lista_100(a,b,c): #sumaLista100
    for i in range(len(a)):
        Suma_lista.append((a[i]+b[i]+c[i])/3) #Promedio de las 3 listas
    return Suma_lista

Suma_lista = []

def suma_lista_100k(a,b,c):#sumaLista100K
    for i in range(len(a)):
        Suma_listak.append((a[i]+b[i]+c[i])/3) #Promedio de las 3 listas
    return Suma_listak

Suma_listak = []

def proceso_cien():#ProcesoCien
    #100 primeros
    m = 0 #Medición 1,2,3
    medicion1 = []
    medicion2 = []
    medicion3 = []
    while m < 3:
        m=m+1
        x = 0 #Número de la sucesión
        while x < 100:
            inicio = default_timer() * 1000
            fib(x)
            fin = default_timer() * 1000
            tiempo = fin - inicio
            x=x+1
            if m == 1:
                medicion1.append(tiempo)
            if m == 2:
                medicion2.append(tiempo)
            if m == 3:
                medicion3.append(tiempo)
    suma_lista_100(medicion1, medicion2, medicion3)
    f = open("ProcesoCien.txt", "a")#Nombre del archivo de 1 a 100 datos de la sucesión.
    for i in Suma_lista:
        f.write((str(i))+"\n")
    f.close()

def proceso_100k():#Proceso100k
    k = 0 # k = cantidad de mediciones
    contador = 0
    medicion_1 = []
    medicion_2 = []
    medicion_3 = []
    while k < 3: 
        k=k+1
        contador = 0
        while contador < 100000:#100k
            contador = contador + 200  #200 en 200 hasta sucesion 100.000 Fib  
            if contador < 100000:#100k
                inicio = default_timer() * 1000
                fib(contador-1)
                fin = default_timer() * 1000
                tiempo = fin - inicio
                if k == 1:
                    medicion_1.append(tiempo)
                if k == 2:
                    medicion_2.append(tiempo)
                if k == 3:
                    medicion_3.append(tiempo)
            else:
                inicio = default_timer() * 1000
                fib(contador-1)
                fin = default_timer() * 1000
                tiempo = fin - inicio
                if k == 1:
                    medicion_1.append(tiempo)
                if k == 2:
                    medicion_2.append(tiempo)
                if k == 3:
                    medicion_3.append(tiempo)
    suma_lista_100k(medicion_1, medicion_2, medicion_3)
    f = open("Nombre_archivo.txt", "a")#Iterativo_Ultimo2 ANAHSE
    for i in Suma_listak:
        f.write((str(i))+"\n")
    f.close()

proceso_cien()
proceso_100k()



