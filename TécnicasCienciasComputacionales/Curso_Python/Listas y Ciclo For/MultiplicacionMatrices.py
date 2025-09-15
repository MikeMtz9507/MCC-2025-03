matrizresultado= []
matriz1= [4,5,6,7,8,9]
matriz2= [2,4,5,6,7,8]
for i in range(len(matriz1)):
    resultado= (matriz1[i] * matriz2[i])
    matrizresultado.append(resultado) #Actualizar mi resultado en la nueva matriz
    print(f"Resultado de las multiplicaciones:",matrizresultado)