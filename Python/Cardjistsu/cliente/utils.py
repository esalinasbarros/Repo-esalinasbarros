import json
from os.path import join

"""
Sacado de la AF3 directamente para utilizar 
los archivos .json (copy/paste)
"""

def data_json(llave):
    ruta = join("parametros.json")
    with open(ruta, "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    valor = diccionario_data[llave]
    return valor


def leer_archivo(ruta):
    with open(ruta, "rb") as archivo:
        bytes_ = archivo.read()
    return bytes_

    
