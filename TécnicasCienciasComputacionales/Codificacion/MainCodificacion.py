from sklearn.preprocessing import LabelEncoder
from streamlit import columns

from KNN import CargaInstancia
import pandas as pd

instancia= CargaInstancia.cargarInstancia("../Archivos/InstanciasTennis.csv")

encoderCielo= LabelEncoder()
encoderTemperatura= LabelEncoder()
encoderHumedad= LabelEncoder()
encoderViento= LabelEncoder()

instancia["Label_Cielo"]= encoderCielo.fit_transform(instancia["Cielo"])
instancia["Label_Temperatura"]= encoderTemperatura.fit_transform(instancia["Temperatura"])
instancia["Label_Humedad"]= encoderHumedad.fit_transform(instancia["Humedad"])
instancia["Label_Viento"]= encoderViento.fit_transform(instancia["Viento"])





instancia= instancia.drop(["Dia","Cielo","Temperatura","Humedad","Viento"], axis=1)

nombre_columnas= list(instancia.columns)

nombre_columnas.pop(nombre_columnas.index("Jugar_tenis"))
nombre_columnas.insert(len(nombre_columnas), "Jugar_tenis")
#print(nombre_columnas)


instancia= instancia[nombre_columnas] #recupera las columnas en el nuevo orden

instancia.to_csv("../Archivos/InstanciaTennisCodLable.csv", index=None)

print()