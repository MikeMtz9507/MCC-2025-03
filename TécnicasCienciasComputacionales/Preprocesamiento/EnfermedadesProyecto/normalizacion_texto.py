import pandas as pd
import re
# from spellchecker import SpellChecker   # lo puedes activar si tienes instalada la librería

# -------------------------
# Cargar archivo original
# -------------------------
df = pd.read_csv("Enfermedades.csv", encoding="latin1")

# -------------------------
# Normalizar nombres de columnas
# -------------------------
df = df.rename(columns={
    "Fieb\\r3": "Fiebre",
    "Dolor     muscular": "Dolor_muscular",
    "DiasSIntomas": "Dias_Sintomas"
})

# -------------------------
# Funciones de limpieza
# -------------------------

# Función para limpiar comentarios o diagnósticos
def limpiar_comentario(texto):
    if pd.isna(texto):
        return ""
    # Quitar espacios extra
    texto = re.sub(r"\s+", " ", str(texto).strip())
    # Mayúscula inicial y punto final
    if texto:
        texto = texto[0].upper() + texto[1:]
        if not texto.endswith("."):
            texto += "."
    return texto

# Función para limpiar Edad
def limpiar_edad(valor):
    if pd.isna(valor):
        return None
    numeros = re.findall(r"\d+", str(valor))
    if numeros:
        return int(numeros[0])
    return None

#Funcion para Limpiar Dia
def limpiar_dia (valor):
    if pd.isna(valor):
        return None
    dia= re.findall( r"\d+", str(valor))
    if dia:
        return int(dia[0])
    return None

# Función para limpiar Fiebre (aquí parece ser temperatura)
def limpiar_fiebre(valor):
    if pd.isna(valor):
        return None
    texto = str(valor).strip().lower()
    # Intentar extraer número decimal
    numeros = re.findall(r"\d+\.?\d*", texto)
    if numeros:
        return float(numeros[0])
    return texto.capitalize()

def corregir_codificacion(texto):
    if isinstance(texto, str):
        try:
            return texto.encode("latin1").decode("utf-8")
        except:
            return texto
    return texto

# -------------------------
# Aplicar limpieza a columnas
# -------------------------
if "Edad" in df.columns:
    df["Edad"] = df["Edad"].apply(limpiar_edad)

if "Dias_Sintomas":
    df["Dias_Sintomas"]= df["Dias_Sintomas"].apply(limpiar_dia)

if "Fiebre" in df.columns:
    df["Fiebre"] = df["Fiebre"].apply(limpiar_fiebre)

if "Enfermedad" in df.columns:
    df["Enfermedad"] = df["Enfermedad"].apply(limpiar_comentario)
    df["Enfermedad"] = df["Enfermedad"].apply(corregir_codificacion)


# -------------------------
# Guardar archivo limpio
# -------------------------
df.to_csv("Enfermedades_limpio.csv", index=False, encoding="utf-8")
print(f"Archivo generado con {len(df)} registros: Enfermedades_limpio.csv")
