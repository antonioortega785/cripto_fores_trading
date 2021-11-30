
import requests
import numpy


def generar_llaves(N):
    '''
    devuelve un arreglo con string con el formato mencionado
    en la funcion 'precios_compra_venta' linea 25
    '''
    vector_llaves =[]

    for i in range(N*4):
        if i <N*2 :
            if i%2 == 0:
                vector_llaves.append('ven' + str(int(i/2)))
            else:
                vector_llaves.append('volv' + str(int(i/2)))
        else:
            if i%2 == 0:
                vector_llaves.append('com' + str(int(i/2 - N)))
            else:
                vector_llaves.append('volc' + str(int(i/2 - N)))
    return vector_llaves

def consultar(mercado, N):
    ''' . retona los N valores mas altos de compra y
        los N valores mas bajos de precios mas bajos de venta
        con su respectivo voloumen
        . retorna un diccionario con 4N registros
        . la forma que se numeran es la siguiente
        ven1, volv1, ven2, volv2, ... , venN, volvN, com1, volc1, com2, volc2, ..., comN, volcN
    '''

    url = f'https://www.buda.com/api/v2/markets/{mercado}/order_book'
    respuesta = requests.get(url)
    ordenes =  respuesta.json().get('order_book')

    precios = []

    for i in range(N):
        precios.append( float(ordenes.get('asks')[i][0]) )
        precios.append( float(ordenes.get('asks')[i][1]) )
    for i in range(N):
        precios.append( float(ordenes.get('bids')[i][0]) )
        precios.append( float(ordenes.get('bids')[i][1]) )

    return precios


print(consultar('btc-cop',3))
