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
                    "mes": mes,
                    "hora": hora,
                    "temp_exterior_c": temp_ext,
                    "temp_interior_c": temp_int,
                    "temp_ac_c": temp_clima
                })
        except Exception as e:
            print(f"Error al procesar fila: {row} ({e})")
            continue



# --- Agrupar por intervalos de tiempo (15, 30, 60 minutos) ---
def promediar_por_intervalo(matriz, intervalo_min):
    if not matriz:
        return []
    matriz_ordenada = sorted(matriz, key=lambda x: x["hora"])

    inicio = matriz_ordenada[0]["hora"]
    fin = inicio + timedelta(minutes=intervalo_min)
    grupo = []
    resultados = []

    for fila in matriz_ordenada:
        if fila["hora"] < fin:
            grupo.append(fila)
        else:
            if grupo:
                ([g["temp_exterior_c"] for g in grupo],[g["temp_interior_c"] for g in grupo])
                resultados.append({
                    "inicio": inicio.strftime("%H:%M"),
                    "prom_temp_exterior": statistics.mean([g["temp_exterior_c"] for g in grupo]),
                    "prom_temp_interior": statistics.mean([g["temp_interior_c"] for g in grupo]),
                    "prom_temp_ac_c": statistics.mean([g["temp_ac_c"] for g in grupo]),

                })
            grupo = [fila]
            inicio = fin
            fin = inicio + timedelta(minutes=intervalo_min)

    # último grupo
    if grupo:
        resultados.append({
            "inicio": inicio.strftime("%H:%M"),
            "prom_temp_exterior": statistics.mean([g["temp_exterior_c"] for g in grupo]),
            "prom_temp_interior": statistics.mean([g["temp_interior_c"] for g in grupo]),
            "prom_temp_ac_c": statistics.mean([g["temp_ac_c"] for g in grupo]),

        })

    return resultados


def mediana_por_intervalo(matriz, intervalo_min= 15 and 30 and 45):
    if not matriz:
        return []
    matriz_ordenada = sorted(matriz, key=lambda x: x["hora"])

    inicio = matriz_ordenada[0]["hora"]
    fin = inicio + timedelta(minutes=intervalo_min)
    grupo = []
    resultados = []

    for fila in matriz_ordenada:
        if fila["hora"] < fin:
            grupo.append(fila)
        else:
            if grupo:
                resultados.append({
                    "inicio": inicio.strftime("%H:%M"),
                    "mediana_temp_exterior": statistics.median([g["temp_exterior_c"] for g in grupo]),
                    "mediana_temp_interior": statistics.median([g["temp_interior_c"] for g in grupo]),
                    "mediana_temp_ac_c": statistics.median([g["temp_ac_c"] for g in grupo]),

                })
            grupo = [fila]
            inicio = fin
            fin = inicio + timedelta(minutes=intervalo_min)

    # último grupo
    if grupo:

        resultados.append({
            "inicio": inicio.strftime("%H:%M"),
            "mediana_temp_exterior": statistics.median([g["temp_exterior_c"] for g in grupo]),
            "mediana_temp_interior": statistics.median([g["temp_interior_c"] for g in grupo]),
            "mediana_temp_ac_c": statistics.median([g["temp_ac_c"] for g in grupo]),

        })

    return resultados


# --- Agrupar por intervalos de tiempo (15, 30, 60 minutos) ---
def estadistica_dia(matriz, intervalo_min=1440):
    if not matriz:
        return []

    resultados = []
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

    for mes in meses:
        datos_mes = [fila for fila in matriz if fila["mes"] == mes]
        if not datos_mes:
            continue

        datos_mes = sorted(datos_mes, key=lambda x: x["hora"])
        inicio = datos_mes[0]["mes"]
        fin = inicio + timedelta(minutes=intervalo_min)
        grupos = []

        for fila in datos_mes:
            if fila["hora"] < fin:
                grupos.append(fila)
            else:
                if grupos:
                    ext = [g["temp_exterior_c"] for g in grupos]
                    inte = [g["temp_interior_c"] for g in grupos]
                    clima = [g["temp_ac_c"] for g in grupos]

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
                inicio = fila["hora"]
                fin = inicio + timedelta(minutes=intervalo_min)
                grupos = [fila]

        # Agregar el último grupo
        if grupos:
            ext = [g["temp_exterior_c"] for g in grupos]
            inte = [g["temp_interior_c"] for g in grupos]
            clima = [g["temp_ac_c"] for g in grupos]

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


# Calcular la mediana de cada 15, 30 y 60 minutos
resultados_15 = mediana_por_intervalo(matriz, 15)
resultados_30 = mediana_por_intervalo(matriz, 30)
resultados_45 = mediana_por_intervalo(matriz, 45)

#resultados_dia= mediana_por_intervalo(matriz,1440)

#Calcular el promedio de cada 15,30 y 60 minutos
resultados_15 = promediar_por_intervalo(matriz, 15)
resultados_30 = promediar_por_intervalo(matriz, 30)
resultados_45 = promediar_por_intervalo(matriz, 45)

resultados_dia = estadistica_dia(matriz,intervalo_min=1440)

#Impresión por día del mes
print("\nPromedios, medianas y correlaciones por día de cada mes (Enero-Junio):\n")
for r in resultados_dia:
    print(
        f"{r['Mes']} (inicio {r['Inicio']}) → "
        f"Prom(ext/int/ac): {r['Promedio Exterior']:.2f}, {r['Promedio Interior']:.2f}, {r['Promedio Clima']:.2f} | "
        f"Med(ext/int/ac): {r['Mediana Exterior']:.2f}, {r['Mediana Interior']:.2f}, {r['Mediana Clima']:.2f} | "
        f"Corr: Ext-Int={r['Corr(Ext-Int)']}, Ext-Clima={r['Corr(Ext-Clima)']}, Int-Clima={r['Corr(Int-Clima)']}"
    )

#Impresión por día de los promedios
print("\n Promedio por día:")
for r in resultados_15:
    print(r)


#Impresión por día de la mediana
print("\n Mediana por dia:")
for r in resultados_15:
    print(r)


#Impresión por día de los promedios
print("\n Promedio por día:")
for r in resultados_30:
    print(r)


#Impresión por día de la mediana
print("\n Mediana por dia:")
for r in resultados_30:
    print(r)

#Impresión por día de los promedios
print("\n Promedio por día:")
for r in resultados_45:
    print(r)


#Impresión por día de la mediana
print("\n Mediana por dia:")
for r in resultados_45:
    print(r)