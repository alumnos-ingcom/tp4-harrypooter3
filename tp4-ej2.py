################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero_1, numero_2):
    temporal = numero_1
    resultado = numero_1 + numero_2
    while temporal != resultado:
        try:
            print(f"{temporal}")
            temporal = temporal + 1
        except:
            break
    return(f"La suma entre el numero {numero_1} y {numero_2} da como resultado {temporal}")

def prueba():
    numero_1 = (int(input("ingrese un numero entero: ")))
    numero_2 = (int(input("ingrese un segundo numero entero: ")))
    print(suma_lenta(numero_1, numero_2))


if __name__ == "__main__":
    prueba()