################
# Ezequiel Sebastian Navone - @harrypooter3
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ordenar_mayor_a_menor(uno, dos, tres):
    lista = list()
    lista.append(uno)
    lista.append(dos)
    lista.append(tres)
    for i in range (1,len(lista)):
        for j in range (len(lista) - i):
            if lista[j] < lista[j + 1]:
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
    return lista
                
def ordenar_menor_a_mayor(uno, dos, tres):
    lista = list()
    lista.append(uno)
    lista.append(dos)
    lista.append(tres)
    for i in range (1,len(lista)):
        for j in range (len(lista) - i):
            if lista[j] > lista[j + 1]:
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
    return lista

def prueba():
    uno = (int(input("Ingresar el primer numero: ")))
    dos = (int(input("Ingresar el segundo numero: ")))
    tres = (int(input("Ingresar el tercer numero: ")))
    lista = ordenar_mayor_a_menor(uno, dos, tres)
    print(f"Lista ordenada de mayor a menor {ordenar_mayor_a_menor(uno, dos, tres)}")
    print(f"Lista ordenada de menor a mayor {ordenar_menor_a_mayor(uno, dos, tres)}")
    


if __name__ == "__main__":
    prueba()
