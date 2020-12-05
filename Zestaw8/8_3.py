import random


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    random.seed()
    k = 0
    for i in range(n):
        x = random.random()  # generuje losowy punkt rzeczywisty między 0 i 1
        y = random.random()  # generuje losowy punkt rzeczywisty między 0 i 1
        if x*x+y*y <= 1:  # jeżeli punkt znajduje się w kole
            k = k+1
    pi = 4*k/n
    print("Obliczona liczba pi =", pi)


if __name__ == '__main__':
    calc_pi(100)
    calc_pi(1000)
    calc_pi(10000)
    calc_pi(100000)
