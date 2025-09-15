
import Metricas as mm
from Metricas import getDistancia

vectorA = [2, 10, 20, 25, 64]
vectorB = [3, 8,20, 25, 56]


# ---------------- MENÚ ----------------
def mostrarmenu():
    print("\n--- Selecciona la distancia a calcular ---")
    print("1. Manhattan")
    print("2. Euclidiana")
    print("3. Chebycheff")
    print("4. Coseno")
    print("5. Euclidiana Promedio")
    print("6. Orloci")
    print("7. Diferencia de Carácter Promedio")
    print("8. Canberra")
    print("9. Sorensen-BrayCurtis")
    print("10. Correlación Pearson")
    print("11. Minkowski (p=3)")
    print("12. Euclidiana Pesada (vectorW = [1,1,1,1,1])")
    print("0. Salir")

while True:
    mostrarmenu()
    opcion = int(input("Elige una opción: "))

    if opcion == 0:
        print("Saliendo...")
        break
    elif opcion == 11:
        distancia = getDistancia(vectorA, vectorB, tipo=opcion, p=3)
    elif opcion == 12:
        distancia = getDistancia(vectorA, vectorB, tipo=opcion, vectorW=[1,1,1,1,1])
    else:
        distancia = getDistancia(vectorA, vectorB, tipo=opcion)

    print(f"Distancia calculada ({opcion}): {distancia}")
