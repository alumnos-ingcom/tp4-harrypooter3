##############
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero1, numero2):
    if numero1 < numero2:
        return -1
    if numero1 == numero2:
        return 0
    if numero1 > numero2:
        return 1

def prueba():
    print("Ingresar dos numeros para sumar ")
    numero1 = (int(input("Ingresar un numero para comparar:")))
    numero2 = (int(input("Ingresar otro numero para comparar: ")))
    print(compara(numero1, numero2))
    
if __name__ == "__main__":
    prueba()