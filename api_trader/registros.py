import pandas as pd
import numpy as np
from pandas import ExcelWriter
import openpyxl
from openpyxl import load_workbook

def lectura (directorio, hoja):
    cuadro = pd.read_excel(directorio, sheet_name = hoja)
    return cuadro
def mercados():

    lista = lectura('datos/api.xlsx', 'mercados').values
    return lista
