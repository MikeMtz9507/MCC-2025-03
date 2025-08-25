import csv

from Preprocesamiento.ejemplomain import lista


#Declarar las variabels como tupla en un Diccionario
map_cielo= {'Sol':1, 'Nubes':2 , 'Lluvia':3}
map_temp= {'Baja': 1 , 'Suave':2, 'Alta':3}
map_humedad= {'Normal':1, 'Alta':2}
map_viento= {'Debil': 1, 'Fuerte':2}
map_jugar= {'Si':1, 'No':0}

#Generar el arreglo Lista, para guardar los valores
Lista= []


#Codigo para leer un archivo CSV
with open('tenis.csv','r', encoding='utf-8') as f:
    reader= csv.reader(f)
    encabezado= next(reader)


idx_cielo= encabezado.index('Cielo')
idx_temp= encabezado.index('Temperatura')
idx_humedad= encabezado.index('Humedad')
idx_viento= encabezado.index('Viento')
idx_jugar= encabezado.index('Jugar_tenis')



lista.append(['Cielo','Temperatura','Humedad','Viento','Jugar_tenis'])


#Generar el recorrido de cada fila de los indices del archivo CSV
for row in reader:
    datos= [

        map_cielo.get([row.idx_cielo], [row.idx_cielo]),
        map_temp.get([row.idx_temp], [row.idx_temp]),
        map_humedad.get([row.idx_humedad], [row.idx_humedad]),
        map_viento.get([row.idx_viento], [row.idx_viento]),
        map_jugar.get([row.idx_jugar], [row.idx_jugar])

    ]

#Guardar los cambios efectuados de los indices en la variable lista
lista.append(datos)

#Recorrer los resultados ya modificados
for fila in lista:

#Imprimir la lista final de datos modificados
    print(lista)




