import CargaInstancia
import Knn_algoritmo

instancia = CargaInstancia.cargarInstancia("../Archivos/InstanciasTennis_Mod1.csv")

import math as m
k = m.sqrt(len(instancia))  # valor inicial de prueba para K
k = int(k)
print("Valor de K: " + str(k))

registro=[9,"Sol","Baja","Normal","Debil","Si"]

Knn_algoritmo.exec(instancia,registro, k)

#for i in range(1,len(instancia)):
#    Knn_algoritmo.exec(instancia, i)

