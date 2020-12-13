import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a+b <= c or b+c <= a or a+c <= b:
        raise ValueError("Podaj długosci boków tak aby utowrzyć trójkąt!!!")
    p = (a+b+c)/2.0
    pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return pole


if __name__ == '__main__':
    print("Obliczam pole trójkąta ze wzoru Herona")
    print("Podaj kolejno dlugosci boków po 'enterze':")
    try:
        a = float(input())
        b = float(input())
        c = float(input())
        try:
            print("Pole trójkąta to :", heron(a, b, c))
        except ValueError:
            print("Podaj dane tak, aby spełniać nierównośc trójkąta!!!")
    except ValueError:
        print("Błędne dane!!!")
