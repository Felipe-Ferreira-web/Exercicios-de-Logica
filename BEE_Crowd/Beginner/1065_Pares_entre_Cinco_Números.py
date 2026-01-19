# Problema: 1065 - Pares entre Cinco Números
# Link: https://judge.beecrowd.com/pt/problems/view/1065
# Categoria: Beginner

entradas = []
pares = 0

while True:
    if len(entradas) < 5:
        entrada = int(input())
        entradas.append(entrada)
        continue
    break

for i in entradas:
    if i % 2 == 0:
        pares = pares + 1


print(f"{pares} valores pares")
