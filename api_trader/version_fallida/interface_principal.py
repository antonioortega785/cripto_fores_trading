import requests
import json

import registros as rg
import funciones as fn
'''
 la siguiente api tiene como objetivo correr 24/7 en un dispositivo de poco poder
 con el fin de hacer actualizaciones de las ordenes de una cuenta buda.com
 las tareas a cumplir son las siguientes:
* generar o cancelar ordenaes al cambiar los precios
    las ordenes se generan cuando un precio es modificado
* hacer un registro de las transacciones efectuada
 '''
'''
market_id = 'btc-cop'
url = f'https://www.buda.com/api/v2/markets/{market_id}/orders'

fn.CLAVE_API = input("api_key")
fn.CLAVE_PRIVADA = input("api_secret")

auth = fn.BudaHMACAuth(api_key_, api_secret)
response = requests.get(url, auth=auth, params={
    'state': 'traded',
    'per': 20,
    'page': 1,
})
print(json.dumps(response.json(),indent=4))
'''
print(fn.precios_default())
