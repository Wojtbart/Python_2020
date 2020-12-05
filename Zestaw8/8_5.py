
def solve2(a, b, c):
    """Rozwiązywanie równania liniowego ax*x + bx + c = 0."""
    if a == 0 and b == 0:
        if c == 0:
            print("Równanie jest nieokreślone")
            return
        else:
            print("Równanie sprzeczne")
            return
    if a == 0:
        print("Jest jedno rozwiązanie: x={}").format(-c/b)
        return
    delta = b*b-4*a*c
    if delta < 0:
        print("Równanie nie ma rozwiązania w liczbach rzeczywistych")
        return
    if delta == 0:
        print("Równanie ma jedno podwójne rozwiązanie: x={}").format(-b/2*a)
        return
    print("Równanie ma dwa rozwiązania: x1={} , x2={}").format(
        (-b-math.sqrt(delta))/(2*a), (-b+math.sqrt(delta))/(2*a))
    return


if __name__ == '__main__':
    print("Podaj kolejno wartości współczynników a,b,c równania kwadratowego:")
    try:
        a = float(input())
        b = float(input())
        c = float(input())
        solve2(a, b, c)
    except ValueError:
        print("Błędne dane!")
