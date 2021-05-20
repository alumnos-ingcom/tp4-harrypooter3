################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def convertir_a_fahrrenheit(centigrados):
    conversion = (int(centigrados * 9/5)) + 32
    return conversion
    
def convertir_a_centigrados(fahrenheit):
    conversion = (fahrenheit -32) * 5/9
    return conversion
    
def prueba():
    centigrados = (float(input("Ingresar grados (en formato de numero) para convertir a fahrenheit: ")))
    fahrenheit = (float(input("Ahora ingresar grados fahrrenheit para convertir a centigrados: ")))
    print(f"Convertiste {centigrados} grados centigrados a {convertir_a_fahrrenheit(centigrados)} grados fahrenheit")
    print(f"Convertiste {fahrenheit} grados fahrenheit a {convertir_a_centigrados(fahrenheit)} grados centigrados")
    

if __name__ == "__main__":
    prueba()