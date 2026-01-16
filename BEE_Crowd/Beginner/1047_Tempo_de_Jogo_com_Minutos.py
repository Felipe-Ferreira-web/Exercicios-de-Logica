# Problema: 1047 - Tempo de Jogo com Minutos
# Link: https://judge.beecrowd.com/pt/problems/view/1047
# Categoria: Beginner

hi, mi, hf, mf = list(map(int, input().split(" ")))


def relogio(hi, mi, hf, mf):
    # Caso para 24h exatas
    if (hi == hf) and (mi == mf):
        return print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

    # Caso para se o jogo começou em um dia e terminou no outro
    elif hi > hf:
        ht = (24 - hi) + hf

    # Caso para se o jogo começou e terminou no mesmo dia
    elif hi < hf:
        ht = hf - hi

    # Caso para se o jogo não teve nem 1h
    elif hi == hf:
        ht = 0

    # Caso para se o jogo começou e terminou na mesma hora e os minutos somados não completaram 1h
    if mi > mf and hi == hf:
        mt = (60 - mi) + mf
        ht = 23

    # Caso para se os minutos já completaram 1h
    elif mi > mf:
        mt = (60 - mi) + mf
        ht = ht - 1

    elif mi < mf:
        mt = mf - mi

    return print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")


relogio(hi, mi, hf, mf)
