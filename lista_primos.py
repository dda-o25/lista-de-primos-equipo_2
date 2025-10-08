"""
Obtener una lista de todos los numeros primos menores a un numero dado
"""

# Declaraciones


# Entradas
numero = int(input("Introduzca su numero: "))
primos = []

# Proceso
for x in range(2, numero + 1):
    es_primo = True
    for i in range(2, x):
        if x % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(x)

# Salidas
texto = ", ".join(map(str,primos))
print(f"Los numeros menores a {numero} son: {texto}.")