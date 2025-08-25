import csv

# Mapas de sustitución -- Utilizando Diccionario
map_sexo = {'Masculino': 1, 'Femenino': 2}
map_jugar = {'Si': 1, 'No': 0}

lista = []

with open('Prueba.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    encabezado = next(reader)  # Leer encabezado completo

    # Buscar los índices de las columnas "Sexo" y "Jugar"
    sexo = encabezado.index('Sexo')
    jugar = encabezado.index('Jugar') if 'Jugar_tenis' in encabezado else encabezado.index('Jugar')

    # Agregar encabezado reducido
    lista.append(['Sexo', 'Jugar'])

    for row in reader:
        # Tomar solo las columnas deseadas
        datos = [row[sexo], row[jugar]]

        # Reemplazar por números
        #datos[0] = map_sexo.get(datos[0], datos[0])
        #datos[1] = map_jugar.get(datos[1], datos[1])

        datos= [

        map_sexo.get(row[sexo],row[sexo]),
        map_jugar.get(row[jugar],row[jugar])

     ]
        lista.append(datos)

# Imprimir matriz completa
for fila in lista:
    print(fila)