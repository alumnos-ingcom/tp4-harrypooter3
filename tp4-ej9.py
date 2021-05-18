################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    numero = int(input("Ingresar un numero entero positivo para saber si es primo o no: "))
    divisor = 2
    contador = 0
    while contador < numero:
        if numero %divisor!=0:
            divisor = divisor + 1
        elif numero == divisor:
            return True
            contador = numero
        else:
            return False
            contador = numero
    return("El numero ingresado tiene que ser mayor a 0")
        
def prueba():
    print (es_primo("Ingresar un numero"))
    
if __name__ == "__main__":
    prueba()