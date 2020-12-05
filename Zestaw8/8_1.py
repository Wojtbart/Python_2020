
'''
Rozwiązaniem równania ax + by = c  nazywamy każdą parę liczb (x_0, y_0),
dla której prawdziwa jest równość ax_0 + by_0 = c.
Rozwiązywanie równania kwadratowego:
1)  Gdy a=0, b=0, c=0 to:
    0=0-> nieskończenie wiele rozwiązań - równanie nieoznaczone
2)  Gdy a=0, b=0, c!=0 to:
    równanie nie ma rozwiązań - równanie sprzeczne
3)  Gdy a=0, b!=0, c!=0 to:
    wynik rozwiązania to prosta prostopadła do osi odciętych(OX) postaci y=-c/b
4)  Gdy a!=0, b=0, c!=0 to:
    wynik rozwiązania to prosta równoległa do osi odciętych(OX) postaci x=-c/a
5)  W pozostałych przypadkach:
    wynik rozwiązania to prosta:
    y=(-ax-c)/b

Algorytm jako lista kroków:
1) PODAJ a, b, c
2) Jeśli a==0 i b==0 to:
        Jeśli c==0:
            WYPISZ: równanie ma nieskończenie wiele rozwiazań
            KONIEC
        W przeciwnym razie:
            WYPISZ: równanie nie posiada rozwiazań
            KONIEC
3) Jeśli a==0:
    WYPISZ: Rozwiązanie to prosta postaci: y=-c/b
    KONIEC
4) Jeśli b==0:
    WYPISZ: Rozwiązanie to prosta postaci: x=-c/a
    KONIEC
5) W każdym przeciwnym razie:
    WYPISZ: Rozwiązanie to prosta postaci y=(-ax-c)/b
    KONIEC
'''


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0:
        if c == 0:
            print("Równanie ma nieskończenie wiele rozwiazań")
            return  # zakończy program
        else:
            print("Równanie ma nieskończenie wiele rozwiazań")
            return
    if a == 0:
        print(("Rozwiązanie to prosta postaci y={}").format(-c/b))
        return
    if b == 0:
        print("Rozwiązanie to prosta postaci x={}").format(-c/a)
        return
    print("Rozwiązanie to prosta postaci y={}x + {}").format(-a/b, -c/b)
    return


if __name__ == '__main__':
    print("Witaj w programie!")
    print("Podaj kolejno po 'enterze' wartości współczynników a,b,c równania liniowego:")
    try:
        a = input()
        b = input()
        c = input()
        # print(a, b, c)
        solve1(a, b, c)
    except ValueError:
        print("Błędne wartosci!")
