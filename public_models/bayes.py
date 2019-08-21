def cnt_PaiPb_ai(n,Pai, Pb_ai: list):
    res = 0.0
    for i in range(n):
        res = res + Pai*Pb_ai[i]
    return res


def cnt_PajPb_aj(Paj, Pb_aj):
    return Paj*Pb_aj