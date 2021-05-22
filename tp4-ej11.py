################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import (IngresoIncorrecto, ingreso_entero)

def ignorar_espacios(texto):
    palindromo = str(texto).replace(' ', '')
    if palindromo == palindromo[::-1]:
         return True
    else:
        return False
        
def ignorar_mayusculas(texto):
    palindromo = str(texto).lower()
    if palindromo == palindromo[::-1]:
        return True
    else:
        return False
        
def ignorar_mayusculas_espacios(texto):
    palindromo = str(texto).lower().replace(' ', '')
    if palindromo == palindromo[::-1]:
         return True
    else:
        return False
        
def es_palindromo(texto):
    palindromo = str(texto)
    if palindromo == palindromo[::-1]:
        return True
    else:
        return False
    
def prueba():
    print("Si el texto a ingresar es una frase con espacios y sin mayusculas escriba 1")
    print("Si el texto a ingresar es un texto con mayusculas y minusculas escriba 2")
    print("Si el texto a ingresar es una combinación de las dos anteriores escriba 3")
    print("Si el texto es solo una palabra sin espacios ni mayusculas escriba 4")
    opcion = int(input("Ingrese una de las cuatro opciones: "))
    texto = (str(input("Ahora ingrese un texto para comprobar si es un palindromo o no: ")))
    if opcion == 1:
        print(ignorar_espacios(texto))
    elif opcion == 2:
        print(ignorar_mayusculas(texto))
    elif opcion == 3:
        print(ignorar_mayusculas_espacios(texto))
    elif opcion == 4:
        print(es_palindromo(texto))  
    else:
        raise IngresoIncorrecto("El numero no es valido, vuelva a intentarlo")
    
if __name__ == "__main__":
    prueba()
