import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Cargar el archivo CSV
df = pd.read_csv("LabelEncoding_Enfermedades.csv")

# Limpiar la columna 'Saturacion' (convertir '99%' a 99.0)
df['Saturacion'] = df['Saturacion'].str.replace('%', '').astype(float)

# Visualizar la distribución original de clases
plt.figure(figsize=(8, 4))
df['Enfermedad'].value_counts().plot(kind='bar')
plt.title("Distribución original de clases")
plt.xlabel("Clase")
plt.ylabel("Número de muestras")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Separar características y variable objetivo
X = df.drop(columns=['Enfermedad'])
y = df['Enfermedad']

# Undersampling
rus = RandomUnderSampler(random_state=42)
X_rus, y_rus = rus.fit_resample(X, y)

plt.figure(figsize=(8, 4))
y_rus.value_counts().plot(kind='bar')
plt.title("Distribución después de Undersampling")
plt.xlabel("Clase")
plt.ylabel("Número de muestras")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Oversampling con SMOTE (n_neighbors=1 para clases pequeñas)
smote = SMOTE(random_state=42, k_neighbors=1)
X_smote, y_smote = smote.fit_resample(X, y)

plt.figure(figsize=(8, 4))
y_smote.value_counts().plot(kind='bar')
plt.title("Distribución después de Oversampling (SMOTE)")
plt.xlabel("Clase")
plt.ylabel("Número de muestras")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
