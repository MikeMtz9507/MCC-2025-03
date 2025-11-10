import pandas as pd
import numpy as np
from sklearn.metrics import mutual_info_score
from sklearn.preprocessing import LabelEncoder
from KNN_Modularizado import CargaInstancia

# =============================================
# CARGAR INSTANCIA
# =============================================
instancia = CargaInstancia.cargarInstancia("../Archivos/iris/iris.csv")
X = instancia.iloc[:, :-1]
y = instancia.iloc[:, -1]

# Convertir etiquetas de clase a números (necesario para cálculos)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# =============================================
# PARÁMETROS DE DISCRETIZACIÓN
# =============================================
v_K = 6  # número de intervalos

# =============================================
# DISCRETIZACIÓN UNIFORME INICIAL
# =============================================
intervalos = []
columns = X.columns
for column in columns:
    auxiliar = X[column]
    v_max = max(auxiliar)
    v_min = min(auxiliar)
    v_width = round((v_max - v_min) / v_K, 4)

    control = round(v_min + v_width, 4)
    temp = [{"inferior": v_min, "superior": control}]

    for j in range(1, v_K - 1):
        control2 = round(control + v_width, 4)
        temp.append({"inferior": control, "superior": control2})
        control = control2

    temp.append({"inferior": control, "superior": v_max})
    intervalos.append(temp)


# =============================================
# FUNCIÓN: Calcular entropía de clase ponderada
# =============================================
def calcular_entropia_ponderada(X_col, y, cortes):
    total = len(X_col)
    entropia_total = 0.0
    for intervalo in cortes:
        mask = (X_col >= intervalo['inferior']) & (X_col < intervalo['superior'])
        y_sub = y[mask]
        if len(y_sub) == 0:
            continue
        proporciones = np.bincount(y_sub) / len(y_sub)
        entropia = -np.sum([p * np.log2(p) for p in proporciones if p > 0])
        entropia_total += (len(y_sub) / total) * entropia
    return entropia_total


# =============================================
# FUNCIÓN: Generar vecinos (ligeros ajustes)
# =============================================
def generar_vecinos(cortes, delta=0.05):
    vecinos = []
    for i in range(1, len(cortes) - 1):  # no mover los extremos
        nuevos_cortes = [dict(c) for c in cortes]  # copia profunda
        # mover punto de corte hacia la izquierda
        nuevos_cortes[i]['superior'] -= delta
        nuevos_cortes[i + 1]['inferior'] -= delta
        vecinos.append(nuevos_cortes)

        # mover punto de corte hacia la derecha
        nuevos_cortes2 = [dict(c) for c in cortes]
        nuevos_cortes2[i]['superior'] += delta
        nuevos_cortes2[i + 1]['inferior'] += delta
        vecinos.append(nuevos_cortes2)
    return vecinos


# =============================================
# FUNCIÓN: Búsqueda Local Iterada
# =============================================
def busqueda_local(X_col, y, cortes, max_iter=20, delta=0.05):
    mejor_cortes = cortes
    mejor_score = calcular_entropia_ponderada(X_col, y, cortes)

    for _ in range(max_iter):
        vecinos = generar_vecinos(mejor_cortes, delta)
        mejor_vecino = None
        for vecino in vecinos:
            score = calcular_entropia_ponderada(X_col, y, vecino)
            if score < mejor_score:
                mejor_score = score
                mejor_vecino = vecino
        if mejor_vecino:
            mejor_cortes = mejor_vecino
        else:
            break  # no mejora
    return mejor_cortes, mejor_score


# =============================================
# APLICAR BÚSQUEDA LOCAL A CADA ATRIBUTO
# =============================================
intervalos_optimizados = []
for i, column in enumerate(columns):
    print(f"\nOptimización para atributo: {column}")
    cortes = intervalos[i]
    mejores_cortes, mejor_entropia = busqueda_local(X[column].values, y_encoded, cortes)
    intervalos_optimizados.append(mejores_cortes)
    print("Mejores cortes:", mejores_cortes)
    print("Entropía:", round(mejor_entropia, 4))

# =============================================
# RESULTADO FINAL
# =============================================
print("\n==== Intervalos optimizados ====")
for col, i in zip(columns, intervalos_optimizados):
    print(f"\nAtributo: {col}")
    for inter in i:
        print(inter)
