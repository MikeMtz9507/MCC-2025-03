import csv
import math as m


#Declaramos nuestro arreglo llamado vectores, en donde guardaremos los valores del archivo
vectores=[]


#Leemos nuestro archivo csv

with open("Vectores.csv", newline= "" ,encoding="utf-8") as csvfile:
 reader = csv.reader(csvfile, delimiter=',')
 next(reader) #Ignoramos la primera fila que tiene encabezados


 for row in reader:
     numeros= [int(x) for x in row] #Convertir cada valor a entero
     vectores.append(numeros)


#Comprobar que hay al menos 2 Vectores
if len(vectores < 2):
    print("El archivo debe contener al menos 2 vectores para caclular las distancias")
else:
 vectorA= [0]
 vectorB =[1]


def getDistancia(vectorA, vectorB, tipo=1, p=1, vectorW=[]):
    match tipo:
        case 1:
            distancia = __Manhattan(vectorA, vectorB)
        case 2:
            distancia = __Euclideana(vectorA, vectorB)
        case 3:
            distancia = __Chebycheff(vectorA, vectorB)
        case 4:
            distancia = __Coseno(vectorA, vectorB)
        case 5:
            distancia = __EuclideanaPromedio(vectorA, vectorB)
        case 6:
            distancia = __Orloci(vectorA, vectorB)
        case 7:
            distancia = __DiferenciaDeCaracterPromedio(vectorA, vectorB)
        case 8:
            distancia = __Canberra(vectorA, vectorB)
        case 9:
            distancia = __Sorensen_BrayCurtis(vectorA, vectorB)
        case 10:
            distancia = __CoeficienteCorrelacionPearson(vectorA, vectorB)
        case 11:
            distancia = __Minkowski(vectorA, vectorB, p)
        case 12:
            distancia = __EuclideanaPesada(vectorA, vectorB, vectorW)
        case _:
            distancia = -1;

    return distancia


# Función de distancia Manhattan
def Manhattan(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise ValueError("Los vectores deben tener la misma longitud.")

    distancia = 0
    for i in range(len(vectorA)):
        distancia += abs(vectorA[i] - vectorB[i])

    return distancia


# Función de distancia Euclidiana
def Euclideana(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise ValueError("Los vectores deben tener la misma longitud.")

    distancia = 0
    for i in range(len(vectorA)):
        distancia += m.pow(vectorA[i] - vectorB[i], 2)

    distancia = m.sqrt(distancia)
    return distancia



# Ejemplo: Calcular las distancias entre el primer y segundo vector
if len(vectores) > 1:
    vectorA = vectores[0]
    vectorB = vectores[1]

    print("\nDistancia Manhattan entre el primer y segundo vector:", Manhattan(vectorA, vectorB))
    print("Distancia Euclidiana entre el primer y segundo vector:", Euclideana(vectorA, vectorB))
