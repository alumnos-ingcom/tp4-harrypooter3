################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    temporal = numero
    resultado = numero + otro_numero
    while temporal != resultado:
        try:
            print(f"{temporal}")
            temporal = temporal + 1
        except:
            break
    return(f"La suma entre el numero {numero} y {otro_numero} da como resultado {temporal}")

def prueba():
    numero = (int(input("ingrese un numero entero: ")))
    otro_numero = (int(input("ingrese un segundo numero entero: ")))
    print(suma_lenta(numero, otro_numero))


if __name__ == "__main__":
    prueba()