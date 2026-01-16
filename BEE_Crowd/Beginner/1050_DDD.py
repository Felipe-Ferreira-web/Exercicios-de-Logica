# Problema: 1049 - DDD
# Link: https://judge.beecrowd.com/pt/problems/view/1050
# Categoria: Beginner

n = int(input())

ddd_map = [
    {"DDD": 61, "Estado": "Brasilia"},
    {"DDD": 71, "Estado": "Salvador"},
    {"DDD": 11, "Estado": "Sao Paulo"},
    {"DDD": 21, "Estado": "Rio de Janeiro"},
    {"DDD": 32, "Estado": "Juiz de Fora"},
    {"DDD": 19, "Estado": "Campinas"},
    {"DDD": 27, "Estado": "Vitoria"},
    {"DDD": 31, "Estado": "Belo Horizonte"},
]


def search_ddd(n):
    for i in ddd_map:
        ddd, estado = i.values()
        if n == ddd:
            return print(estado)
    return print("DDD nao cadastrado")


search_ddd(n)
