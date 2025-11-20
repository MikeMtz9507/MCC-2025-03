import csv
import statistics
from datetime import datetime, timedelta

matriz = []

# --- Lectura del CSV (Mes, Hora, TempExt, TempInt, TempClima) ---
with open("explicación.csv", newline='', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)
    for row in lector:
        try:
            mes = row[0]
            hora = datetime.strptime(row[1], "%H:%M")

            temp_ext = float(row[2])
            temp_int = float(row[3])
            temp_clima = float(row[4])

            matriz.append({
                "mes": mes,
                "hora": hora,
                "temp_exterior": temp_ext,
                "temp_interior": temp_int,
                "temp_clima": temp_clima
            })

        except Exception as e:
            print(f"Error en fila {row} ({e})")
            continue


# --- Correlación manual ---
def correlacion_manual(x, y):
    if len(x) < 2 or len(y) < 2:
        return None
    media_x = statistics.mean(x)
    media_y = statistics.mean(y)
    num = sum((xi - media_x)*(yi - media_y) for xi, yi in zip(x,y))
    den = (sum((xi - media_x)**2 for xi in x) * sum((yi - media_y)**2 for yi in y))**0.5
    return None if den == 0 else round(num/den, 3)


# --- Detectar días automáticos (sin columna Día) ---
def separar_por_dias(datos):
    dias = []
    dia_actual = []
    hora_anterior = datos[0]["hora"]

    for fila in datos:
        if fila["hora"] < hora_anterior:  # cambio de día
            dias.append(dia_actual)
            dia_actual = []
        dia_actual.append(fila)
        hora_anterior = fila["hora"]

    if dia_actual:
        dias.append(dia_actual)

    return dias


# --- Estadísticas cada 15 minutos por día ---
def calcular_estadisticas(matriz):
    resultados = []
    meses = sorted(set(f["mes"] for f in matriz))

    for mes in meses:
        datos_mes = sorted(
            [f for f in matriz if f["mes"] == mes],
            key=lambda x: x["hora"]
        )

        dias = separar_por_dias(datos_mes)

        for num_dia, datos_dia in enumerate(dias, start=1):

            # Filtrar horario 7:00–20:00
            datos_dia = [
                f for f in datos_dia
                if 7 <= f["hora"].hour < 20
            ]

            inicio = datetime(2025,1,1,7,0)
            fin = inicio + timedelta(minutes=30)

            while inicio.hour < 20:
                grupo = [
                    f for f in datos_dia
                    if inicio.time() <= f["hora"].time() < fin.time()
                ]

                if grupo:
                    ext = [g["temp_exterior"] for g in grupo]
                    inte = [g["temp_interior"] for g in grupo]
                    clima = [g["temp_clima"] for g in grupo]

                    resultados.append({
                        "Mes": mes,
                        "Dia": num_dia,
                        "Inicio": inicio.strftime("%H:%M"),
                        "Fin": fin.strftime("%H:%M"),
                        "Promedio_exterior": statistics.mean(ext),
                        "Promedio_interior": statistics.mean(inte),
                        "Promedio_clima": statistics.mean(clima),
                        "Corr(Ext-Clima)": correlacion_manual(ext, clima),
                        "Corr(Int-Clima)": correlacion_manual(inte, clima)
                    })

                inicio = fin
                fin = inicio + timedelta(minutes=30)

    return resultados


# --- Ejecutar ---
resultados_15min = calcular_estadisticas(matriz)


print("\nPrimeros resultados:\n")
for r in resultados_15min:
    print(r)


# --- Guardar CSV ---
nombre_salida = "resultados_eda_dia_30min.csv"
with open(nombre_salida, "w", newline="", encoding="utf-8") as f:
    campos = [
        "Mes","Dia","Inicio","Fin",
        "Promedio_exterior","Promedio_interior","Promedio_clima",
        "Corr(Ext-Clima)","Corr(Int-Clima)"
    ]
    w = csv.DictWriter(f, fieldnames=campos)
    w.writeheader()
    w.writerows(resultados_15min)

print(f"\nResultados guardados en '{nombre_salida}'.")
