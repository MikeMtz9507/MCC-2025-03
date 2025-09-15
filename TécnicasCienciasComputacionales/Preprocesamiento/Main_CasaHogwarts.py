import csv
import math as m
def toInt(set):
    for item in range(len(set)):
        for j in range(len(set[item])):
            set[item][j] = int(set[item][j])
    return set

lista = []
with open('Casa de Hogwarts.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for fila in read:
        lista.append(fila[1:])

casas = {'Gryffindor':1, 'Slytherin':2, 'Hufflepuff':3, 'Ravenclaw':4}

header = lista.pop(0)
for fila in lista:
    valor_actual = fila[-1]  # última columna
    fila[-1] = casas[valor_actual]

lista = toInt(lista)

caso1 = [35,28,90,33,43,11,37,59]

resultados = list()
opcion= int(input("Ingresa el valor a ejecutar"))
j = 0
distancia = 0

for fila in range(len(lista)):
    for columna in range(len(lista[fila])-1):
        # Manhattan
        if(opcion==1):
            j = j + 1
            distancia += abs(lista[fila][columna]-caso1[j])
            print(f"La distancia Manhattan es:",distancia)
            resultados.append(distancia)
            print(resultados[0])
        #Eudclideana
        elif(opcion==2):
            j = j + 1
            distancia += pow(abs(lista[fila][columna]-caso1[j]),2)
            print(f"La distancia Euclideana es: ", distancia)
            resultados.append(distancia)
            print(resultados[0])
        #Euclideana Promedio
        elif(opcion==3):
            j = j + 1
            distancia += m.pow(lista[fila][columna]- caso1[j], 2)
            distancia = distancia / (lista[fila][columna])
            distancia = m.sqrt(distancia)
            resultados.append(distancia)
            print(resultados[0])
        else:
            print("Opción inválida. Debes ingresar 1 ,2 o 3.")
        break

