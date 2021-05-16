################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    numero = int(input("Ingresar un numero entero positivo para saber si es primo o no: "))
    Divisor = 2
    Contador = 0
    while Contador < numero:
        if numero %Divisor!=0:
            Divisor = Divisor + 1
            return False
        elif numero == Divisor:
            return True
            Contador = numero
        else:
            return False
            Contador = numero
    print("El numero ingresado tiene que ser mayor a 0")
        
def prueba():
    print (es_primo("Ingresar un numero"))
if __name__ == "__main__":
    prueba()