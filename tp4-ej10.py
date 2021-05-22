################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factores_primos(numero):
    lista = list()
    for i in range(2, numero + 1):
        while numero % i == 0:
            lista.append(i)
            numero = numero / i
    return lista
    
def prueba():
    numero = int(input("Ingresar un numero para descomponer en sus factores primos: "))
    lista = factores_primos(numero)
    print(f"{factores_primos(numero)}")

if __name__ == "__main__":
    prueba()
