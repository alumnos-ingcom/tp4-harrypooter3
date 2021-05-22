################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " # ")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("Te quedaste sin intentos") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    while cantidad_reintentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto:
            cantidad_reintentos = cantidad_reintentos - 1
            print(f"Numero incorrecto, te queda la cantidad de {cantidad_reintentos} reintento/s")
    raise IngresoIncorrecto("Te quedaste sin intentos")
                     
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    rango = (int(input("Ingrese un valor entre 0 y 10: ")))
    if (rango >= 0 and rango <=10):
        return(f"El numero que ingreso es {rango}")
    else:
        raise IngresoIncorrecto("No ingresaste un numero correcto")


def prueba():
    print(ingreso_entero_reintento("ingresa un numero entero"))
    print(ingreso_entero_restringido("ingresa un numero entero"))

if __name__ == "__main__":
    prueba()