import random
import sys


# algorytm euklidesa,zwraca nwd(najwiekszy wspólny dzielnik) liczb a i b(https://pl.wikipedia.org/wiki/Algorytm_Euklidesa)
def gcd(a, b):
    while b != 0:
        # a, b = b, a % b
        c = a % b
        a = b
        b = c
    return a


# rozszerzony algorytm Euklidesa(https://pl.wikipedia.org/wiki/Algorytm_Euklidesa)
# zwraca nwd,wsp. przy największej liczbie, wsp. przy najmniejszej liczbie, np dla
# nwd(174,18) zwraca 6,-1,10 --------> 6=(-1)*174+10*18
def extGcd(a, b):

    x, y = 1, 0
    r, s = 0, 1

    while (b != 0):
        c = a % b
        q = a//b
        a = b
        b = c

        x, r = r, x-q*r
        y, s = s, y-q*s
    return a, x, y


# do sprawdzenia czy liczba jest pierwsza(zwraca True lub False)
def isPrime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# zwraca 2 losowe liczby pierwsze
def drawPrimeNumber():
    L = []
    while len(L) != 2:
        x = random.randint(2, 1000)
        if isPrime(x):
            L.append(x)
    return L


# generowanie pary kluczy: publicznego i prywatnego
def generateKeyPair(p, q):
    # iloczyn liczb pierwszych
    n = p*q

    # funkcja sumy(totient, funkcja eulera)
    phi = (p-1)*(q-1)

    # wybieramy liczbe losową e (1<e<phi)
    e = random.randrange(2, phi)

    # algorytm euklidesa do sprawdzenia czy e i phi są względnie pierwsze
    # wybieramy liczbe losową e dopóki e i phi są względnie pierwsze, czyli gcd(e,phi)=1
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)

    # bierzemy wsp. x oraz y przy najwiekszej i najmniejszej potedze
    nwd, x, y = extGcd(e, phi)

    # upewniamy się, że d(klucz prywatny) jest dodatnie
    if (x < 0):
        d = x + phi
    else:
        d = x

    # zwraca np. publiczny klucz(e=39,n=391) oraz prywatny klucz(d=27,n=391)
    return((e, n), (d, n))


# funkcja do zaszyfrowania
def encrypt(privateKey, text):
    # rozbijamy klucz
    key, n = privateKey

    # konwertujemy każdą literę w tekście jako liczba Unicode używając a^b mod m()
    encrypted = [((ord(char) ** key) % n) for char in text]

    return encrypted


# funkcja do deszyfrowania
def decrypt(publicKey, text):
    # rozbijamy klucz
    key, n = publicKey
    text = text

    # Generujemy tekst z klucza i zaszyforwanego tekstu a^b mod m
    decrypted = [chr((char ** (key)) % n) for char in text]

    # dołączamy tekst po literze
    return ''.join(decrypted)


if __name__ == '__main__':

    choose = input('Czy chcesz sam wygenerować klucze publiczne(t lub n)')
    if (choose == 't'):
        p = int(input("Wpisz większą liczbę pierwszą (31,37,41,43 itd.):"))
        q = int(input("Wpisz inną liczbę pierwszą (jakiej jeszcze nie wpisałeś):"))
    elif(choose == 'n'):
        p = drawPrimeNumber()[0]
        q = drawPrimeNumber()[1]
    else:
        print("Niepoprawna opcja, zamykam program!")
        sys.exit(0)  # gdy zła to kończę program
    print("Generowanie pary kluczy . . .")

    public, private = generateKeyPair(p, q)
    print("Klucz publiczny to ", public, " i klucz prywatny to ", private)

    message = input("Wpisz wiadomośc do zaszyfrowania: ")

    encryptedMsg = encrypt(private, message)
    print("Zaszyfrowana wiadomość:")
    print(''.join(map(str, encryptedMsg)))

    print("Rozszyfrowana wiadomość:")
    print(decrypt(public, encryptedMsg))
