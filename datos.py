import time
import llamadas
import guardado

from pynput import keyboard as kb

estados_posibles = {
    's':'salida',
    'e':'ejecucion',
    'i':'interrumpido'
}
estados_programa = 'i'

def pulsa(tecla):

    global estados_programa
    estados_programa = str(tecla)

    if tecla == kb.KeyCode.from_char('s'):
        return False
    elif tecla == kb.KeyCode.from_char('e'):
        estados_programa = 'e'
    elif tecla == kb.KeyCode.from_char('i'):
        estados_programa = 'i'

escuchador = kb.Listener(pulsa)
escuchador.start()

'''
     definen 5 ofertas distintas de compra y venta
'''
numero_ofertas = 5
latencia = 3.5
ruta_archivo = 'archivo.xlsx'
mercado = 'btc-usdc'

while escuchador.is_alive():


    for clave in estados_posibles:
        print(clave, " : ", estados_posibles[clave])
    print('\n')
    print('Estod actual: ',estados_programa)

    if estados_programa == 'e':


        datos = llamadas.consultar(mercado, numero_ofertas)
        datos.append(time.strftime("%d/%m/%y"))
        datos.append(time.strftime("%H:%M:%S"))

        guardado.guardar2(datos, ruta_archivo)
        print(datos)
        '''
        claves = llamadas.generar_llaves(numero_ofertas)
        claves.append('fecha')
        claves.append('hora')

        buffer = {}

        for i in range(numero_ofertas*4 + 2):
            buffer[claves[i]] = datos[i]

        print(buffer)

        guardado.guardar(buffer, ruta_archivo) '''

        time.sleep(latencia)
    time.sleep(0.5)
    pass
