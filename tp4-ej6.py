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
    num_minimo = lista[0]
    for j in lista:
        if (num_minimo >  j):
            num_minimo = j
    return num_minimo
    
def maximo(lista):
    num_maximo = lista[0]
    for i in lista:
        if (num_maximo < i):
            num_maximo = i
    return num_maximo
        
def prueba():
    cantidad = int(input("Cantidad de numeros: "))
    rangomin = int(input("Rango Minimo: "))
    rangomax = int(input("Rango Maximo (superior al rango minimo): "))
    lista = lista_aleatoria(cantidad, rangomin, rangomax)
    print(lista)
    print(f"El menor numero es {minimo(lista)}")
    print(f"El mayor numero es {maximo(lista)}")
    
if __name__ == "__main__":
    prueba()