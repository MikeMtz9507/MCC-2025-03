import csv
import statistics
from datetime import datetime, timedelta
from scipy.stats import pearsonr

matriz = []

# --- LECTURA DEL CSV ---
with open("explicación.csv", newline='', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)  # saltar encabezado si lo tiene
    for row in lector:
        try:
            mes = row[0]
            hora = datetime.strptime(row[1], "%H:%M")
            temp_ext = float(row[2])
            temp_int = float(row[3])
            temp_clima = float(row[4])

            if mes in ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]:
                matriz.append({
                    "Mes": mes,
                    "Hora": hora,
                    "temp_exterior": temp_ext,
                    "temp_interior": temp_int,
                    "temp_clima": temp_clima
                })
        except Exception as e:
            print(f"Error al procesar fila: {row} ({e})")
            continue


# --- AGRUPAR Y CALCULAR POR DÍA (SUPONIENDO 1440 MINUTOS = 1 DÍA) ---
def calcular_estadisticas_diarias(matriz, intervalo_min=15):
    if not matriz:
        return []

    resultados = []
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

    for mes in meses:
        datos_mes = [fila for fila in matriz if fila["Mes"] == mes]
        if not datos_mes:
            continue

        datos_mes = sorted(datos_mes, key=lambda x: x["Hora"])
        inicio = datos_mes[0]["Hora"]
        fin = inicio + timedelta(minutes=intervalo_min)
        grupos = []

        for fila in datos_mes:
            if fila["Hora"] < fin:
                grupos.append(fila)
            else:
                if grupos:
                    ext = [g["temp_exterior"] for g in grupos]
                    inte = [g["temp_interior"] for g in grupos]
                    clima = [g["temp_clima"] for g in grupos]

                    resultados.append({
                        "Mes": mes,
                        "Inicio": inicio.strftime("%H:%M"),
                        "Promedio Exterior": statistics.mean(ext),
                        "Promedio Interior": statistics.mean(inte),
                        "Promedio Clima": statistics.mean(clima),
                        "Mediana Exterior": statistics.median(ext),
                        "Mediana Interior": statistics.median(inte),
                        "Mediana Clima": statistics.median(clima),
                        "Corr(Ext-Int)": round(pearsonr(ext, inte)[0], 3) if len(ext) > 1 else None,
                        "Corr(Ext-Clima)": round(pearsonr(ext, clima)[0], 3) if len(ext) > 1 else None,
                        "Corr(Int-Clima)": round(pearsonr(inte, clima)[0], 3) if len(inte) > 1 else None
                    })
                # Reiniciar el grupo
                inicio = fila["Hora"]
                fin = inicio + timedelta(minutes=intervalo_min)
                grupos = [fila]

        # Agregar el último grupo
        if grupos:
            ext = [g["temp_exterior"] for g in grupos]
            inte = [g["temp_interior"] for g in grupos]
            clima = [g["temp_clima"] for g in grupos]

            resultados.append({
                "Mes": mes,
                "Inicio": inicio.strftime("%H:%M"),
                "Promedio Exterior": statistics.mean(ext),
                "Promedio Interior": statistics.mean(inte),
                "Promedio Clima": statistics.mean(clima),
                "Mediana Exterior": statistics.median(ext),
                "Mediana Interior": statistics.median(inte),
                "Mediana Clima": statistics.median(clima),
                "Corr(Ext-Int)": round(pearsonr(ext, inte)[0], 3) if len(ext) > 1 else None,
                "Corr(Ext-Clima)": round(pearsonr(ext, clima)[0], 3) if len(ext) > 1 else None,
                "Corr(Int-Clima)": round(pearsonr(inte, clima)[0], 3) if len(inte) > 1 else None
            })

    return resultados


# --- EJECUCIÓN ---
#resultados_dia = calcular_estadisticas_diarias(matriz, 1440)
resultados_dia = calcular_estadisticas_diarias(matriz, 15 and 30 and 45)
# --- IMPRESIÓN ---
print("\nPromedios, medianas y correlaciones por día de cada mes (Enero-Junio):\n")
for r in resultados_dia:
    print(
        f"{r['Mes']} (inicio {r['Inicio']}) → "
        f"Prom(ext/int/ac): {r['Promedio Exterior']:.2f}, {r['Promedio Interior']:.2f}, {r['Promedio Clima']:.2f} | "
        f"Med(ext/int/ac): {r['Mediana Exterior']:.2f}, {r['Mediana Interior']:.2f}, {r['Mediana Clima']:.2f} | "
        f"Corr: Ext-Int={r['Corr(Ext-Int)']}, Ext-Clima={r['Corr(Ext-Clima)']}, Int-Clima={r['Corr(Int-Clima)']}"
    )
