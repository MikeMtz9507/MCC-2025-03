import csv

#Utilizar dirección para sustitución de varibales
sexo= {'Masculino': 1, 'Femenino': 2},
activo= {'Si': 1, 'No': 0}

#Declarar la variable lista
lista= []

#Utilizar libreria CSV para abrir archivo
with open('Registro.csv', 'r', encoding = 'utf-8') as f:
     reader= csv.reader(f)
     encabezado= next(reader)


#Hacer busqueda de indice de las columnas seleccionadas

idx_sexo= encabezado.index('Sexo')
idx_activo= encabezado.index('Activo')


#Generar los encabezados para la nueva lista
lista.append(['Sexo','Activo'])


# Procesar filas
for row in reader:
        datos = {

            sexo.get(row[idx_sexo], row[idx_sexo]),
            activo.get(row[idx_activo], row[idx_activo])

        }

        #Guardar los nuevos registros en la tabla
        lista.append(datos)

#Imprimir
for fila in lista:
    print(fila)
