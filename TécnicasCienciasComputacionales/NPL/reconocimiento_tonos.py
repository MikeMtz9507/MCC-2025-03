import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

# 1. Dataset de ejemplo
data = {
    "comentario": [
        "Me encantó el servicio, todo fue rápido y fácil",
        "El personal fue muy grosero y nada amable",
        "La atención estuvo bien, nada fuera de lo normal",
        "Estoy muy satisfecho con la biblioteca",
        "No me gustó la experiencia, perdí mucho tiempo",
        "El servicio fue aceptable",
        "Excelente atención, lo recomiendo",
        "Muy mala organización, no regresaré"
    ],
    "tono": [
        "positivo",
        "negativo",
        "neutral",
        "positivo",
        "negativo",
        "neutral",
        "positivo",
        "negativo"
    ]
}

df = pd.DataFrame(data)

# 2. División de datos
X = df["comentario"]
y = df["tono"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Pipeline con TF-IDF + Naive Bayes
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())

# 4. Entrenar
modelo.fit(X_train, y_train)

# 5. Evaluar
y_pred = modelo.predict(X_test)
print("Reporte de clasificación:\n")
print(classification_report(y_test, y_pred))

# 6. Probar con comentarios nuevos
nuevos = [
    "El servicio fue increíble, estoy muy contento",
    "Nunca me habían tratado tan mal",
    "Todo estuvo regular, nada especial"
]

predicciones = modelo.predict(nuevos)
for comentario, tono in zip(nuevos, predicciones):
    print(f"Comentario: '{comentario}' → Tono: {tono}")



#RECONOCIMIENTO
#TfidfVectorizer: convierte los comentarios en representaciones numéricas.
#MultinomialNB: un modelo de clasificación muy usado en texto.
# classification_report: muestra métricas de precisión, recall y F1.
#Al final, el modelo predice si un comentario nuevo es positivo, negativo o neutral.
