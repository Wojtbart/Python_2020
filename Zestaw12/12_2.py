import random


# zwraca indeks elementu w tablicy
def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if right is None:
        right = len(L) - 1
    if left > right:
        print("Brak elementu !")
        return False

    # ustalamy środek
    mid = (left+right)//2

    if(y == L[mid]):
        return mid
    elif(y < L[mid]):
        return binarne_rek(L, left, mid-1, y)
    else:
        return binarne_rek(L, mid+1, right, y)


if __name__ == '__main__':
    L = [random.choice(range(10)) for i in range(15)]
    L.sort()
    element = 5  # szukany element

    print("Lista L =" + str(L))
    print("Szukamy {} w liscie L".format(element))
    print("Indeks {}: {}".format(element, binarne_rek(L, 0, len(L) - 1, element)))
