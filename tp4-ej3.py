################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def convertir_a_fahrrenheit(centigrados):
    grados = (float(input("Ingresar grados (en formato de numero) para convertir a fahrrenheit: ")))
    conversion = (grados * 9/5) + 32
    print(f" Convertiste {grados} grados centigrados a {conversion} grados fahrrenheit")
    
def convertir_a_centigrados(fahrenheit):
    grados = (float(input("Ahora ingresar grados fahrrenheit para convertir a centigrados: ")))
    conversion = (grados -32) * 5/9
    print(f" Convertiste {grados} grados centigrados a {conversion} grados fahrrenheit")
    
def prueba():
    print(convertir_a_fahrrenheit("Ingresar grados centigrados"))
    print(convertir_a_centigrados("Ingresar grados fahrrenheit"))
    

if __name__ == "__main__":
    prueba()