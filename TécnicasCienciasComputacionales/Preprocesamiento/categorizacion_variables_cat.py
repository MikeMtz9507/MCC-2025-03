import csv

from urllib3.filepost import writer

# Mapas de sustitución
map_categoria = {'Alumno':1,'Docente':2,'Personal Administrativo':3,'Otro':4}
map_amabilidad = {'Muy Malo':1,'Malo':2,'Neutral':3,'Bueno':4,'Muy Bueno':5}
map_asesoria = {'Muy Malo':1,'Malo':2,'Neutral':3,'Bueno':4,'Muy Bueno':5}
map_rapidez ={'Muy Malo':1,'Malo':2,'Neutral':3,'Bueno':4,'Muy Bueno':5}


# Función para clasificar Evaluación
def clasificar_evaluacion(valor):
    try:
        valor = float(valor)
        if 0 <= valor <= 3:
            return "Muy Malo"
        elif 3 < valor <= 5:
            return "Malo"
        elif 5 < valor <= 7:
            return "Neutral"
        elif 7 < valor <= 9:
            return "Bueno"
        elif valor == 10:
            return "Muy Bueno"
        else:
            return "Fuera del rango de evaluación"
    except ValueError:
        return "Dato inválido"


lista = []

with open('instanciabiblioteca.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    encabezado = next(reader)  # Leer encabezado completo

    # Buscar los índices de las columnas "Sexo" y "Jugar"
    idx_categoria = encabezado.index('Categoria')
    idx_evaluacion= encabezado.index('Evaluación')
    idx_amabilidad = encabezado.index('Amabilidad')
    idx_asesoria = encabezado.index('Asesorias')
    idx_rapidez = encabezado.index('Rapidez')

    # Agregar encabezado reducido
    lista.append(['Categoria','Evaluación','Amabilidad','Asesorias','Rapidez'])


    for row in reader:
        datos = [
            map_categoria.get(row[idx_categoria], row[idx_categoria]),
            clasificar_evaluacion(row[idx_evaluacion]),
            map_amabilidad.get(row[idx_amabilidad], row[idx_amabilidad]),
            map_asesoria.get(row[idx_asesoria], row[idx_asesoria]),
            map_rapidez.get(row[idx_rapidez], row[idx_rapidez])
        ]
        lista.append(datos)

# Imprimir matriz completa
for fila in lista:
    print(fila)


#Guardar nuevos registros CSV
    with open('etiquetado_datos.csv','w', newline='', encoding='utf-8-sig') as f:
        writer= csv.writer(f)
        writer.writerow(lista)
        print ("Se ha guardado el archivo exitosamente")