from P05_KNN_Modularizado import CargaInstancia
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# ================================================================
# 1. Cargar instancia original
instancia = CargaInstancia.cargarInstancia("../Archivos/iris/iris.csv")

#############################################################################################
### GRUPOS A GENERAR (Discretización)
v_K = 6
#############################################################################################
columns = instancia.columns[:-1]  # atributos sin la clase

for column in columns:  # por atributo
    aux = 0
    instancia.sort_values(column, inplace=True)
    instancia.reset_index(inplace=True, drop=True)

    # convertir a string para multinomial
    instancia[column] = instancia[column].astype("str")

    for k in range(v_K):
        for j in range(int(len(instancia) / v_K)):
            instancia.loc[aux, column] = "var" + str(k + 1)
            aux += 1

# Guardar dataset discretizado
instancia.to_csv("../Archivos/iris/instancia_discretizada_EFB.csv", index=False)

print("\nArchivo discretizado guardado.\n")

# ================================================================
# 2. Cargar dataset discretizado para Naive Bayes
data = pd.read_csv("../Archivos/iris/instancia_discretizada_EFB.csv")

X = data.iloc[:, :-1]   # atributos
y = data.iloc[:, -1]    # clase

# One-hot encoding para variables categóricas (requerido por sklearn)
X_encoded = pd.get_dummies(X)

# ================================================================
# 3. Entrenar y evaluar Naive Bayes
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

nb = MultinomialNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

print("==== Resultados Naive Bayes ====")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReporte de Clasificación:\n", classification_report(y_test, y_pred))
