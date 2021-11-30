import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def sim(numero, media, varianza, fluctuacion, picos):
    datos = np.random.normal(media, varianza, numero)

    for i in range(numero):
        datos[i] = datos[i]*( 1 + (fluctuacion*np.sin(picos* i/180)))

    return datos

def suma(datos):
    suma = 0
    for i in datos:
        suma = suma + i
    return suma
def vector_pesos_1(numero_datos):
    pesos = []
    i = numero_datos
    while i>2:
        i = int(i/2)
        pesos.append(i)
    return pesos[::-1]

def media_ver_1(cola, pesos, suma_pesos, valor_insertar):

    n = len(cola.datos)

    media_actual = cola.media_actual*(n+ suma_pesos) - cola.datos[((cola.cabeza)%n)]

    for i in range(len(pesos)):
        media_actual = media_actual - cola.datos[(n-pesos[i]+cola.cabeza)%n]
    media_actual = media_actual + valor_insertar*(len(pesos)+1)
    return ( media_actual/(n+ suma_pesos))

def media_ver_1_init(cola, pesos):

    sumando = 0
    pes_actual = 0
    n = len(cola.datos)

    for i in range(n):
        if pes_actual < len(pesos):
            if i == pesos[pes_actual]:
                pes_actual  = pes_actual+1
        sumando = sumando + cola.datos[(cola.cabeza-1+n-i)%n]*(len(pesos)-pes_actual + 1)
    return sumando/(n+suma(pesos))

class cola:
    def __init__(self, longitud, media_actual= 0.1):
        self.datos = np.random.normal(0,1,longitud)
        self.cabeza = 0
        self.media_actual = media_actual
    def insertar(self, dato):
        self.datos[int(self.cabeza)] = float(dato)
        self.cabeza = (self.cabeza+1)%len(self.datos)
    def reset_datos(self, valor):
        for i in range(len(self.datos)):
            self.datos[i] = valor
