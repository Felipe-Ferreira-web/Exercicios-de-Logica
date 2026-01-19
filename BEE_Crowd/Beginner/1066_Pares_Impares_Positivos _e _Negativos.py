# Problema: 1066 - Pares, Ímpares, Positivos e Negativos
# Link: https://judge.beecrowd.com/pt/problems/view/1066
# Categoria: Beginner

entradas = []
positivos = 0
negativos = 0
pares = 0
impares = 0

while True:
    if len(entradas) < 5:
        entrada = int(input())
        entradas.append(entrada)
        continue
    break


for i in entradas:
    if i > 0:
        positivos = positivos + 1
    if i < 0:
        negativos = negativos + 1
    if i % 2 == 0:
        pares = pares + 1
    if i % 2 != 0:
        impares = impares + 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
