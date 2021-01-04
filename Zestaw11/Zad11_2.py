# Do sortowania wykorzystuję algorytm quicksort
# Stworzyłem funkcję zapisującą dane do plików sortX.dat, gdzie X=1,2,3,4,5
# Nastepnie za pomocą tych plików rysuję obrazki sortX.png, gdzie X=1,2,3,4,5 w gnuplocie
# Wszystkie pliki znajdują się w folderze data
# Korzystam z losowych danych z zadania 11_1.py
# Kod pisze na Windowsie w Visual Studio Code, uzywam Pythona w wersji 3.9, tutaj też w trakcie działania programu mogę sobie kliknąc na dany obrazek i zobaczyć na żywo jak program sortuje dane

from Zad11_1 import *
import time
import subprocess


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item


def saveFile(L, filename):
    file = open(filename, 'w')
    nrFile = filename[9]  # data/sort1.dat
    size = len(L)
    for i in range(0, size):
        file.write('{} {}\n'.format(str(i), str(L[i])))
    file.close()

    # wykonuje komendy z gnuplota używając biblioteki subprocess oraz piszę na stdin
    plot = subprocess.Popen(
        ['gnuplot', '-p'], shell=True, stdin=subprocess.PIPE)

    plot.stdin.write('set term png\n'.encode("utf-8"))
    plot.stdin.write('set output "data/sort{}.png"\n'.format(
        nrFile).encode("utf-8"))
    plot.stdin.write('set title "Sortowanie X"\n'.encode("utf-8"))
    plot.stdin.write('set xlabel "numer pozycji"\n'.encode("utf-8"))
    plot.stdin.write('set ylabel "liczba na pozycji"\n'.encode("utf-8"))
    plot.stdin.write('unset key\n'.encode("utf-8"))
    plot.stdin.write('plot "{}" using 1:2 with points pt 5\n'.format(
        filename).encode("utf-8"))
    # odczekuje sekundę
    time.sleep(1)


def quicksort(L, left, right, filename):

    if left >= right:
        return
    swap(L, left, (left + right) // 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1, filename)
    quicksort(L, pivot + 1, right, filename)
    saveFile(L, filename)


if __name__ == '__main__':
    number = 50
    L1 = createRandInt(number)
    L2 = createSomeRandIntSort(number)
    L3 = createRandIntSortReverse(number)
    L4 = createRandFloatGauss(number)
    L5 = createRandIntSet(number)

    quicksort(L1, 0, number-1, "data/sort1.dat")
    quicksort(L2, 0, number-1, "data/sort2.dat")
    quicksort(L3, 0, number-1, "data/sort3.dat")
    quicksort(L4, 0, number-1, "data/sort4.dat")
    quicksort(L5, 0, number-1, "data/sort5.dat")
