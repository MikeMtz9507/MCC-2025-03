import csv
lista= []
with open('tenis.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        #Imprimir fila
        lista.append(row[1:])



for i in range(1, len(lista)):
    #if lista[i][1] == 'Sol':
        #lista[i][1] = 1
    #elif lista[i][2] == 'Lluvia':
         #lista[i][2] = 2
    #elif lista[i][3] == 'Nubes':
         #lista[i][3] = 3
    if lista[i][2] == 'Sol':
        lista[i][2] = 1
    elif lista[i][3] == 'Lluvia':
         lista[i][3] = 2
    elif lista[i][4] == 'Nubes':
         lista[i][4] = 3
for e in lista:
    print(e)

    #Imprimir la matriz
    #print()
    #Imprimir la primera fila y elemento de la matriz
    print("\nImprimir primer elemento de la segunda fila",lista[1][1])


