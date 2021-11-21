import pandas as pd
from pandas import ExcelWriter

import openpyxl
from openpyxl import load_workbook

alfabeto =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def guardar(datos, directorio):

    df = pd.read_excel(directorio)
    df = df.append(datos, ignore_index = False)
    df.to_excel(directorio)
    return True

def guardar2(datos, directorio):

    libro = load_workbook(directorio)
    hoja = libro.active

    n_registros = int(hoja['A1'].value)

    for i in range(len(datos)):
        celda = alfabeto[i+1]+ str(n_registros)
        hoja[celda] = datos[i]

    hoja['A1'] = n_registros +1

    libro.save(directorio)
