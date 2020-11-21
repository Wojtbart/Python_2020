from fractions import gcd


def reduction(nomin, denomin):
    gcdNum = gcd(nomin, denomin)
    return [nomin / gcdNum, denomin / gcdNum]


def add_frac(frac1, frac2):        # frac1 + frac2
    nominator = frac1[0]*frac2[1]+frac2[0]*frac1[1]
    denominator = frac1[1]*frac2[1]
    return reduction(nominator, denominator)


def sub_frac(frac1, frac2):         # frac1 - frac2
    nominator = frac1[0]*frac2[1]-frac2[0]*frac1[1]
    denominator = frac1[1]*frac2[1]
    return reduction(nominator, denominator)


def mul_frac(frac1, frac2):         # frac1 * frac2
    nominator = frac1[0]*frac2[0]
    denominator = frac1[1]*frac2[1]
    return reduction(nominator, denominator)


def div_frac(frac1, frac2):       # frac1 / frac2
    nominator = frac1[0]*frac2[1]
    denominator = frac1[1]*frac2[0]
    return reduction(nominator, denominator)


def is_positive(frac):              # bool, czy dodatni
    if frac[0] < 0:
        if frac[1] < 0:
            return True
        else:
            return False
    elif frac[1] < 0:
        return False
    elif frac[0] == 0:
        return False
    else:
        return True


def is_zero(frac):                 # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2):       # -1 | 0 | +1
    if frac1[0]/frac1[1] < frac2[0]/frac2[1]:
        return -1
    elif frac1[0]/frac1[1] == frac2[0]/frac2[1]:
        return 0
    else:
        return 1


# konwersja do float, dzielenie w pythonie3 zwraca float, nie trzeba rzutować
def frac2float(frac):
    return float(frac[0]/frac[1])
