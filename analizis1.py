import guardado
import numpy as np
import matplotlib.pyplot as plt

def punto_corte(precios, media):
    for i in range(len(precios)):
        if precios[i]>media:
            return i
def conteo_real(precios):
    n = 0
    anterior = precios[0]
    for i in precios:
        if anterior < i:
            n = n +1
        anterior = i
    return n

datos_guardados = guardado.lectura('archivo.xlsx','Sheet1')
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

media = [media_ventas,  media_compras, media_total]
maximo = [ventas[-1], compras[-1]]
minimo = [ventas[0], [compras[0]]]
superacion = [len(ventas), ((len(ventas)-punto_corte(compras, media_ventas))*100/len(ventas)), ((punto_corte(ventas, media_compras))*100/len(ventas))]

rentabilidad = [compras[-1]-ventas[1], (compras[-1]- ventas[1])*100/compras[-1]]
cambio_ofertas = [conteo_real(ventas), conteo_real(compras)]

print(" media                 : ", media)
print(" maximo                : ", maximo)
print(" minimo                : ", minimo)
print(" rantabilidad          : ", rentabilidad)
print(" superacion de medias  : ",superacion)
print(" conteo real de ventas : ", cambio_ofertas)

plt.plot(ventas_sin)
plt.plot(compras_sin)
plt.show()
