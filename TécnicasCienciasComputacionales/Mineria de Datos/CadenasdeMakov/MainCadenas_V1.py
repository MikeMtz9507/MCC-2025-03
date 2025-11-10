from sympy import content

archivo= open("MatrizdeEstados.csv")
content= archivo.readlines()
print(content)
instancia= [i.split(",") for i in content]
print(instancia)
matriz= [list(map(float,i)) for i in instancia]
print(matriz)

print(matriz)

for fila in matriz:
    print(fila)
