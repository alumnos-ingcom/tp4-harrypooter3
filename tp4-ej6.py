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
    NumMinimo = lista[0]
    for j in lista:
        if (NumMinimo > j):
            NumMinimo = j
    print(f"{NumMinimo} es el menor numero de la lista")
def maximo(lista):
    pass
        
def prueba():
    Cantidad = int(input("Cantidad de numeros: "))
    Rangomin = int(input("Rango Minimo: "))
    Rangomax = int(input("Rango Maximo (superior al rango minimo): "))
    print (lista_aleatoria(Cantidad,Rangomin,Rangomax))
    print (minimo)
if __name__ == "__main__":
    prueba()