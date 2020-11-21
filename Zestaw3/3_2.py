# 3.2 Co jest zlego w kodzie
if __name__ == "__main__":

    L = [3, 5, 4]
    L = L.sort()
    # Przypisujemy zmiennej l wywołanie funkcji sort na liście L, podczas gdy metoda sort() sortuje listę w
    # miejscu, nie zwraca nowej wartosci, L.sort() zwraca None

    x, y = 1, 2, 3
    # nie wiadomo którą wartośc chcieliśmy przyporządkować do którejś zmiennej(ValueError), za mało zmiennych, nierówne długości sekwencji

    X = 1, 2, 3
    X[1] = 4
    # X jest krotką, nie można jej modyfikować , ponieważ ma ustalony rozmiar

    X = [1, 2, 3]
    X[3] = 4
    # W liscie elementy liczymy od 0, więc indeks 3 wychodzi poza listę

    X = "abc"
    X.append("d")
    # metodę append możemy wykonywać tylko na listach a X jest stringiem(stringi są niezmienne)

    L = list(map(pow, range(8)))
    # metoda pow podnosząca liczbe do wyzbnaczonej potegi potrzebuje 2 argumentow, a ma podany 1 argument
