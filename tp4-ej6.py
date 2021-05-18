##############
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from random import randint

def lista_aleatoria(cantidad, minimo, maximo):
    lista = list()
    for i in range(cantidad):
        try:
            lista.append(randint(minimo, maximo))
        except ValueError as err:
            print("El numero maximo tiene que ser superior al minimo")
            break
    return lista
        
def minimo(lista):
    numminimo = lista[0]
    for j in lista:
        if (numminimo > j):
            numminimo = j
    print(f"{numminimo} es el menor numero de la lista")
def maximo(lista):
    pass
        
def prueba():
    cantidad = int(input("Cantidad de numeros: "))
    rangomin = int(input("Rango Minimo: "))
    rangomax = int(input("Rango Maximo (superior al rango minimo): "))
    print (lista_aleatoria(cantidad,rangomin,rangomax))
    print (minimo)
if __name__ == "__main__":
    prueba()