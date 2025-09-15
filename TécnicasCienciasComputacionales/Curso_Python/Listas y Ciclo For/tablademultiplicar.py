#1 Ejercicio de Tabla de Multiplicar:
num= int(input("Ingresa el número para la tabla de multiplicar"))
print(f'Tabla de multiplicar del número{num}')
for i in range(0,11):
    result= num* i
    print(f"{num} x {i} = {result}")
#########-------------------------------------########
#2 Ejercicio de For anidados de tabla de multiplicar

for i in range (1,11):
    print("-------")
    print(f"Tabla del {i}")
    for j in range(1,11):
        result= i * j
        print(f"{i}x{j} = {result}")
        print("------")
        print()

