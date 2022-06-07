def etox(x, tollerance):
    n = 1
    term  = 1
    tox = 0
    cnt  = 0

    while term > tollerance:
        tox += term
        cnt += 1
        term = term * x/n
        n += 1

    return tox, cnt

def eTox(x, tolerance):
    term = 1
    cnt = 1
    summ = 0

    while abs(term) > tolerance:
        summ += term
        term = term * x / cnt
        cnt += 1

    return summ, cnt-1


t,c = eTox(1,1e-15)
print(t)
print(c)

t,c = etox(1,1e-15)
print(t)
print(c)