import numpy as np
import matplotlib.pyplot as plt

import metodo1 as m1
from primera_prueba import guardado

def media(cola, valor_insetar):
    return (cola.media_actual*len(cola.datos) - cola.datos[(len(cola.datos)+cola.cabeza)%len(cola.datos)] + valor_insetar)/len(cola.datos)
def media_init(cola):
    sumatoria = 0
    for i in cola.datos:
        sumatoria = sumatoria + i
    return sumatoria/len(cola.datos)


datos_guardados = guardado.lectura('primera_prueba//archivo.xlsx','Sheet1')
datos_guardados = datos_guardados.reset_index().values
datos_guardados = datos_guardados.T

ventas_sin = datos_guardados[2]
compras_sin = datos_guardados[12]
hora = datos_guardados[23]
ventas = np.sort(ventas_sin)
compras = np.sort(compras_sin)

media_ventas = np.mean(ventas)
media_compras = np.mean(compras)
media_total = (media_ventas+media_compras) / 2


mercado = m1.sim(10000, 5500, 50, 0.03, 0.2)

muestreo = m1.cola(1000, 0)
muestreo.reset_datos(5500)

pesos_ = m1.vector_pesos_1(1000)
suma_p = m1.suma(pesos_)

muestreo2 = m1.cola(1000, 0)
muestreo2.reset_datos(5500)

muestreo3 = m1.cola(1000, 0)
muestreo3.reset_datos(5500)

pesos_2 = pesos_ * 2

print("extructuras generadas")


muestreo.media_actual = m1.media_ver_1_init(muestreo, pesos_)
muestreo2.media_actual = media_init(muestreo2)
muestreo3.media_actual = m1.media_ver_1_init(muestreo3, pesos_)

recoleccion_muestas = []
media_estandar = []
recoleccion_muestas_2 = []

diferencia = []

print("analizando ... ")

for i in mercado:
    muestreo.media_actual = m1.media_ver_1(muestreo, pesos_, suma_p, i)
    recoleccion_muestas.append(muestreo.media_actual )
    muestreo.insertar(i)

    muestreo2.media_actual = media(muestreo2, i)
    media_estandar.append( muestreo2.media_actual)
    muestreo2.insertar(i)

    muestreo3.media_actual = m1.media_ver_1(muestreo3, pesos_2, suma_p*2, i)
    recoleccion_muestas_2.append(muestreo3.media_actual)
    muestreo3.insertar(i)

    diferencia.append(5500+muestreo2.media_actual-muestreo.media_actual)

print("analizis completo")


recoleccion_muestas_for = np.array(recoleccion_muestas)
media_estandar_for = np.array(media_estandar)
recoleccion_muestas_2_for = np.array(recoleccion_muestas_2)
diferencia_for = np.array(diferencia)

plt.plot(mercado, color='black')
plt.plot(recoleccion_muestas_for, color='orange')
plt.plot(media_estandar_for, color='blue')
plt.plot(recoleccion_muestas_2_for, color='red')
plt.plot(diferencia_for, color='yellow')

plt.show()
