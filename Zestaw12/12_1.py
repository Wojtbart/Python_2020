import random

n = 100  # ilosc liczb
scope = 10  # zakres do losowania liczb
L = []  # lista L
# szukana randomowa liczba z zakresu 0 do scope-1
searchNumber = random.randint(0, scope-1)
counter = 0  # licznik do liczenia wystąpień w liście L


def linear_search(L, left, right, y):
    """Wyszukiwanie liniowe w ciągu."""
    i = left
    while i <= right:
        if y == L[i]:
            return i
        i += 1
    return None


def pushElements(n, scope):
    for i in range(0, n):
        L.append(random.randint(0, scope-1))


def findnumber(number):
    global counter
    i, numberPlace = 0, 0
    while(i < n):
        # miejsce na którym wystapila liczba
        numberPlace = linear_search(L, i, n-1, number)
        # print(numberPlace)
        if(numberPlace == None):
            break
        i = numberPlace+1  # zwiekszam i bo wczesniej nie ma już tej liczby
        counter += 1


if __name__ == '__main__':
    pushElements(n, scope)
    print(L)
    findnumber(searchNumber)
    print('Liczba {} wystąpiła {} razy w liscie L'.format(searchNumber, counter))
