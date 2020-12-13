class SingleList:
    # ... inne metody ...

    def remove_tail(self): pass   # klasy O(N)
    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other): pass   # klasy O(1)
    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.

    def clear(self): pass     # czyszczenie listy
