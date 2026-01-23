# Problema: 1072 - Intervalo 2
# Link: https://judge.beecrowd.com/pt/problems/view/1072
# Categoria: Beginner

num = int(input())
entradas = []
dentro = 0
fora = 0

while True:
    if len(entradas) < num:
        entrada = int(input())
        entradas.append(entrada)
        continue
    break

for i in entradas:
    if i >= 10 and i <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print(f"{dentro} in")
print(f"{fora} out")
