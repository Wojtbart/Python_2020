import time
# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.


def P(i, j):
    if i < 0 or j < 0:
        raise ValueError("i oraz j muszą być dodatanie!!!")
    P = [[0 for x in range(j+1)] for y in range(i+1)]
    for k in range(i+1):
        for l in range(j+1):
            if k == 0 and l == 0:
                P[k][l] = 0.5
            elif k > 0 and k == 0:
                P[k][l] = 0.0
            elif k == 0 and l > 0:
                P[k][l] = 1.0
            else:
                P[k][l] = 0.5 * (P[k - 1][l] + P[k][l - 1])
                # print(P[k][l])
    return P[i][j]


def Prek(i, j):
    if i < 0 or j < 0:
        raise ValueError("i oraz j muszą być dodatanie!!!")
    elif i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (Prek(i-1, j) + Prek(i, j-1))


if __name__ == '__main__':

    #P.dictionary = {(0, 0): 0.5, (1, 0): 0.0, (0, 1): 1.0}

    start = time.time()
    print("Wywołanie P dynamicznie:", P(10, 15))
    timeP = time.time() - start
    start = time.time()
    print("Wywołanie P rekurencyjnie:", Prek(10, 15))
    timePrek = time.time() - start

    print("Czas dynamicznie: "+str(round(timeP, 8))+"s")
    print("Czas rekurecyjnie: "+str(round(timePrek, 8))+"s")
