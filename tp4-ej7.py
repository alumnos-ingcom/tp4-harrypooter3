################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def division_lenta(dividendo, divisor):
    if (dividendo > 0 and divisor > 0):
        cociente = 0
        resto = dividendo
        while resto >= divisor:
            resto = resto - divisor
            cociente = cociente +1
        print(f" El cociente es igual a {cociente}")
        print(f" El resto es {resto}")
    else:
        raise IngresoIncorrecto("No ingresaste un numero correcto")
        
def prueba():
    print("Ingresar dos numeros para hacer la resta")
    dividendo = int(input("Ingresar el dividendo: "))
    divisor = int(input("Ingresar el divisor: "))
    print(division_lenta(dividendo, divisor))

if __name__ == "__main__":
    prueba()
