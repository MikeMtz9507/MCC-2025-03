import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("LabelEncoding_Enfermedades.csv")

# Función para clasificar la frecuencia cardíaca
def clasificar_fc(fc):
    if fc < 60:
        return "Baja"
    elif 60 <= fc <= 100:
        return "Normal"
    else:
        return "Alta"

# Función para clasificar la presión arterial
def clasificar_presion(sistolica, diastolica):
    if sistolica > 140 or diastolica > 90 or sistolica < 90 or diastolica < 60:
        return "Riesgo"
    else:
        return "Normal"

# Función para clasificar la frecuencia respiratoria
def clasificar_fr(fr):
    if fr < 12:
        return "Baja"
    elif 12 <= fr <= 20:
        return "Normal"
    elif 21 <= fr <= 24:
        return "Checate Porfa"
    else:
        return "Alta"

# Aplicar las funciones y crear nuevas columnas
df["FC_clasificacion"] = df["Frecuencia_cardiaca"].apply(clasificar_fc)
df["Presion_clasificacion"] = df.apply(lambda row: clasificar_presion(row["Presion_sistolica"], row["Presion_diastolica"]), axis=1)
df["FR_clasificacion"] = df["Frecuencia_respiratoria"].apply(clasificar_fr)

# Guardar el nuevo archivo con clasificaciones
df.to_csv("Enfermedades_clasificadas.csv", index=False, encoding="utf-8")
