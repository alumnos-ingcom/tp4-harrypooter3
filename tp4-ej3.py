################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def convertir_a_fahrrenheit(centigrados):
    conversion = (int(centigrados * 9/5)) + 32
    return(f" Convertiste {centigrados} grados centigrados a {conversion} grados fahrrenheit")
    
def convertir_a_centigrados(fahrenheit):
    conversion = (fahrenheit -32) * 5/9
    return(f" Convertiste {fahrenheit} grados centigrados a {conversion} grados fahrrenheit")
    
def prueba():
    centigrados = (float(input("Ingresar grados (en formato de numero) para convertir a fahrrenheit: ")))
    fahrenheit = (float(input("Ahora ingresar grados fahrrenheit para convertir a centigrados: ")))
    print(convertir_a_fahrrenheit(centigrados))
    print(convertir_a_centigrados(fahrenheit))
    

if __name__ == "__main__":
    prueba()