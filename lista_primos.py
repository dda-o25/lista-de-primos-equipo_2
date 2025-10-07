"""
Obtener una lista de todos los numeros primos menores a un numero dado
"""

# Declaraciones


# Entradas
numero = int(input("Introduzca su numero: "))
primos = []

# Proceso
for x in range(2,numero):
    es_primo = True
    for i in range(2, x):
        if x % i == 0:
            es_primo = False
            break
        if es_primo:
            primos.append(x)

# Salidas
print("Los numeros primos menores a", numero, "son: ", primos)