import pandas as pd
import math as m
from pandas.core.interchange.dataframe_protocol import DataFrame

#Lectura de archivo CSV
instancia= pd.read_csv("matrices.csv")

#Convierte encabezado y toma los valores númericos de la instancia
matriz= instancia.values


#Se genera una matriz, en donde se guardaran los resultados de las distancias calculadas
#distancias=[]
#Selecciona el tipo de distancia
print("Selecciona la ecuación que deseas calcular")
print("1 - Manhattan")
print("2 - Euclidiana")
opcion= int(input("Ingresa tu opción (1 o 2):"))


#Calculas las distancias segun las opciones ejecutadas

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if opcion == 1:
            #Se calcula la distancia manhattan
            distancia= sum(abs(matriz[i]- matriz [j]))
            print(f"Distancia Manhattan entre fila {i + 1} y fila {j + 1}: {distancia}")
        elif opcion == 2:
            #Se calcula la distancia euclideana
            distancia= pow(abs(matriz[i]- matriz [j]), 2)
            print(f"Distancia Euclidiana entre fila {i + 1} y fila {j + 1}: {distancia}")
        else:
            print("Opción inválida. Debes ingresar 1 o 2.")
        break



#for i in range(len(matriz)):
    #fila=[]
    #for j in range(len(matriz)):
        #Calcular la distancia manhattan
        #distancia = sum(abs(matriz[i] - matriz[j])) #Generamos el cálculo de la distancia manhattan
        #fila.append(distancia) #Guardamos esa distancia en la lista fila.
        #distancias.append(distancia) #Al terminar con todos los j, guardamos esa fila completa en la matriz de distancias.
        #Se imprime el resultado de cada distancia calculada
        #print(f"Distancia Manhattan entre fila {i + 1} y fila {j + 1}: {distancia}")


#for i in range(len(matriz)):
    #fila=[]
    #for j in range(len(matriz)):
        #distancia += m.pow(matriz[i] - matriz[j], 2) #Generamos el cálculo de la distancia euclideana
        #distancia = m.sqrt(distancia)
#print(f"Distancia Manhattan entre fila {i + 1} y fila {j + 1}: {distancia}")
#Se guardan los registros de cada fila en un Dataframe
#df= pd.DataFrame(distancias)

# Guardarmos el DataFrame en un archivo CSV
#df.to_csv('Distancia_Manhattan.csv', index=False)


#print("Archivo 'Distancia_Manhattan.csv' generado correctamente!")
