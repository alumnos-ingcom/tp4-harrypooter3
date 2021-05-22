##############
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    if numero == 0:
        return "0"
    if numero > 0:
        return "+" 
    if numero < 0:
        return "-"
        

def prueba():
    numero = (int(input("Ingresar un numero entero para ver si es positivo, negativo o cero: ")))
    print(signo(numero))
    
if __name__ == "__main__":
    prueba()