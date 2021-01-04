import random
import math


def createRandInt(n):
    L = list(range(0, n))
    random.shuffle(L)  # zmieniamy kolejnośc w liście
    return L


def createSomeRandIntSort(n):
    L = list(range(0, n))
    alfa = round(math.log(n)*2)
    for i in range(0, n):
        x = i-alfa
        y = i+alfa
        x = 0 if x < 0 else x
        y = n-1 if y >= n else y

        rand = random.randint(x, y)
        L[i], L[rand] = L[rand], L[i]
    return L


def createRandIntSortReverse(n):
    L = createSomeRandIntSort(n)
    return L[::-1]


def createRandFloatGauss(n):
    mu, sigma = 0, 1
    L = [round(random.gauss(mu, sigma), 2)
         for i in range(0, n)]  # zaokraglam do 2 miejsc po przecinku
    return L


def createRandIntSet(n):
    end = math.floor(math.sqrt(n))
    L = [random.randint(0, end) for i in range(n)]
    return L


if __name__ == '__main__':
    number = 20
    print(createRandInt(number))
    print(createSomeRandIntSort(number))
    print(createRandIntSortReverse(number))
    print(createRandFloatGauss(number))
    print(createRandIntSet(number))
