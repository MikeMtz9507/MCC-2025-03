
import pandas as pd
import numpy as np

# 1- Cargar la instancia CSV
df = pd.read_csv("../Archivos/InstanciaTennis.csv")

# 2. Identificar cuántas clases distintas hay
clases = df["Play Tennis"].unique()
print("Clases encontradas:", clases)

# 3. Calcular la cantidad de registros por clase
conteo_clases = df["Play Tennis"].value_counts()
print("Cantidad de registros por clase:")
print(conteo_clases, "\n")

# 4. Definir porcentaje para entrenamiento (ej. 70%)
porcentaje_entrenamiento= float(input("Ingresa el valor de porcentaje para el entrenamiento del modelo:"))

# 5. Calcular cuántos registros tomar por clase para el entrenamiento
muestras_por_clase = (conteo_clases * porcentaje_entrenamiento).astype(int)
print("Registros que se tomarán por clase:")
print(muestras_por_clase, "\n")

# 6. Seleccionar aleatoriamente los registros por estratificación
# ============================================================
df_train = pd.DataFrame()

for clase, cantidad in muestras_por_clase.items():
    df_clase = df[df["Play Tennis"] == clase]
    df_train = pd.concat([df_train, df_clase.sample(n=cantidad, random_state=42)])

print("Dataset de entrenamiento estratificado:")
print(df_train.sort_values("Play Tennis"), "\n")

# 7. Guardar resultados
df_train.to_csv("dataset_estratificadotennis.csv", index=False, encoding="utf-8-sig")
print("Archivo 'dataset_estratificadotennis.csv' creado correctamente.")