import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sympy import false

df= pd.read_csv("Enfermedades_limpio.csv")

# Inicializar codificadores
encoder_tos= LabelEncoder()
encoder_dolormuscular= LabelEncoder()
encoder_exposicion= LabelEncoder()
encoder_fatiga= LabelEncoder()
encoder_dolorgarganta= LabelEncoder()
encoder_dolorcabeza = LabelEncoder()
encoder_escalofrios = LabelEncoder()
encoder_perdidaolfato = LabelEncoder()
encoder_congestionnasal = LabelEncoder()
encoder_doloroido = LabelEncoder()
encoder_tosflema = LabelEncoder()
encoder_vacunado = LabelEncoder()
encoder_alergias = LabelEncoder()


# Aplicar Label Encoding a cada columna
df["Tos"]= encoder_tos.fit_transform(df["Tos"])
df["Dolor_muscular"]= encoder_dolormuscular.fit_transform(df["Dolor_muscular"])
df["Exposicion"]= encoder_exposicion.fit_transform(df["Exposicion"])
df["Fatiga"] = encoder_fatiga.fit_transform(df["Fatiga"])
df["Dolor_garganta"]= encoder_dolorgarganta.fit_transform(df["Dolor_garganta"])
df["Dolor_cabeza"]= encoder_dolorcabeza.fit_transform(df["Dolor_cabeza"])
df["Escalofrios"]= encoder_escalofrios.fit_transform(df["Escalofrios"])
df["Perdida_olfato"] = encoder_perdidaolfato.fit_transform(df["Perdida_olfato"])
df["Congestion_nasal"] = encoder_congestionnasal.fit_transform(df["Congestion_nasal"])
df["Dolor_oido"] = encoder_doloroido.fit_transform(df["Dolor_oido"])
df["Tos_con_flema"] = encoder_tosflema.fit_transform(df["Tos_con_flema"])
df["Vacunado"] = encoder_vacunado.fit_transform(df["Vacunado"])
df["Alergias_previas"] = encoder_alergias.fit_transform(df["Alergias_previas"])


#Guardar archivo como nuevo
df.to_csv("LabelEncoding_Enfermedades.csv", index=false, encoding="utf-8")



#Imprimir guardar archivo
print("Se ha guardado con exito el archivo LabelEncoding_Enfermedades.csv")

