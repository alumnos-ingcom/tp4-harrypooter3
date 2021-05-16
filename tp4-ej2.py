################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero_1):
    numero_1 = (int(input("ingrese un numero entero: ")))
    numero_2 = (int(input("ingrese un segundo numero entero: ")))
    Temporal = numero_1
    Resultado = numero_1 + numero_2
    while Temporal != Resultado:
        try:
            print(f"{Temporal}")
            Temporal = Temporal + 1
        except:
            break
    print(f"La suma entre el numero {numero_1} y {numero_2} da como resultado {Temporal}")

def prueba():
    print(suma_lenta("Ingresar un numero entero"))

if __name__ == "__main__":
    prueba()