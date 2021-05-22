################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import IngresoIncorrecto

def division_lenta(dividendo, divisor):
    if (dividendo > 0 and divisor > 0):
        cociente = 0
        resto = dividendo
        while resto >= divisor:
            resto = resto - divisor
            cociente = cociente +1
        return(cociente, resto)
    else:
        raise IngresoIncorrecto("No ingresaste un numero correcto")
        
def prueba():
    print("Ingresar dos numeros para hacer la resta")
    dividendo = int(input("Ingresar el dividendo: "))
    divisor = int(input("Ingresar el divisor: "))
    cociente, resto = division_lenta(dividendo, divisor)
    print(f"El cociente es {cociente} y el resto es {resto}")

if __name__ == "__main__":
    prueba()
