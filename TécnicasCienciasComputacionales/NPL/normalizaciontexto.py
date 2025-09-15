import pandas as pd
import re
from spellchecker import SpellChecker

# Cargar archivo con la codificación correcta
df = pd.read_csv("instanciaservicioune.csv", encoding="latin1")

# Inicializar corrector ortográfico en español
spell = SpellChecker(language='es')

def limpiar_comentario(texto):
    if pd.isna(texto):
        return ""

    # 1. Normalizar caracteres mal codificados (ej. Ã± → ñ)
    try:
        texto = texto.encode("latin1").decode("utf-8")
    except:
        pass

    # 2. Quitar espacios extra
    texto = re.sub(r"\s+", " ", texto.strip())

    # 3. Corregir ortografía palabra por palabra
    palabras = texto.split()
    corregidas = []
    for palabra in palabras:
        if palabra.lower() not in spell:  # si no está en diccionario
            corregidas.append(spell.correction(palabra) or palabra)
        else:
            corregidas.append(palabra)

    texto = " ".join(corregidas)

    # 4. Manejo de mayúscula inicial y punto final
    if texto:
        texto = texto[0].upper() + texto[1:]
        if not texto.endswith("."):
            texto += "."

    return texto

# Aplicar limpieza
df["Comentarios_Limpios"] = df["Comentarios"].apply(limpiar_comentario)

# Guardar a nuevo CSV (no sobreescribe el original)
df.to_csv("instanciaservicioune_limpio.csv", index=False, encoding="utf-8-sig")

print("Archivo generado: instanciaservicioune_limpio.csv")
