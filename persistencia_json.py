import json


def store(variable, archivo):
    variable = input(print("variable: "))
    archivo = input(print("archivo: "))
    json.dump(json.dumps(archivo), open(archivo, "w"))


def retrieve(archivo):
    return json.load
