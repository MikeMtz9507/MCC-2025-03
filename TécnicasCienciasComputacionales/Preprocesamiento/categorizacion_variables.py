import csv

# Mapas de sustitución --- Utilizando Tupla en Diccionario
cielo = {'Sol': 1, 'Lluvia': 2, 'Nubes': 3}
temp = {'Alta': 1, 'Baja': 2, 'Suave': 3}
humedad = {'Alta': 1, 'Normal': 2}
viento = {'Debil': 1, 'Fuerte': 2}
jugar = {'No': 0, 'Si': 1}


#Se genera una variable lista, donde se guardara la lista actualizada
lista = []


#Libreria CSV para leer archivo
with open('tenis.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    encabezado = next(reader)

# Buscar índices de columnas
    idx_cielo = encabezado.index('Cielo')
    idx_temp = encabezado.index('Temperatura')
    idx_humedad = encabezado.index('Humedad')
    idx_viento = encabezado.index('Viento')
    idx_jugar = encabezado.index('Jugar_tenis')

# Agregar encabezado a la lista final
    lista.append(['Cielo', 'Temperatura', 'Humedad', 'Viento', 'Jugar_tenis'])

# Procesar filas con su indice
    for row in reader:
        datos = [
            cielo.get(row[idx_cielo], row[idx_cielo]),
            temp.get(row[idx_temp], row[idx_temp]),
            humedad.get(row[idx_humedad], row[idx_humedad]),
            viento.get(row[idx_viento], row[idx_viento]),
            jugar.get(row[idx_jugar], row[idx_jugar])
        ]
        lista.append(datos)

# Imprimir matriz modificada
for fila in lista:
    print(fila)
