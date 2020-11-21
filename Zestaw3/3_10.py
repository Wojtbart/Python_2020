# 3.10

# Sposoby na tworzenie słownika tłumaczącego liczby rzymskie na arabskie

# 1.słownik{klucz:wartośc}
Dictionary = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# 2.stworzenie slownika za pomoca konstruktora
Dictionary2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

# 3.stworzenie slownika za pomoca listy tupli
Dictionary3 = [("I", 1), ("V", 5), ("X", 10), ("L", 50),
               ("IC", 100), ("D", 500), ("M", 1000)]

# 4.stworzenie slownika i zainicjowanie wszystkich kluczy ta sama wartoscia, w tym przypadku 0 i nastepnie przyporzadkowanie kazdemu kluczowi odpowiedniej wartosci
DictionaryData = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
Dictionary4 = dict.fromkeys(DictionaryData, 0)
Dictionary4['V'] = 5
Dictionary4['X'] = 10
Dictionary4['L'] = 50
Dictionary4['C'] = 100
Dictionary4['D'] = 500
Dictionary4['M'] = 1000

# 5. Stworzenie dwóch list i połączenie ich za pomoca metody zip
DictionaryKeys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
DictionaryValue = [1, 5, 10, 50, 100, 500, 1000]

merge = dict(zip(DictionaryKeys, DictionaryValue))

# -------------
# -------------
# -------------

# funkcja roman2int() nie sprawdza poprawnosci syntaktycznej liczb rzymskich, np (VV) bedzie dla niego 10


def roman2int(romanStr):
    result = 0
    for x in range(len(romanStr)):
        s1 = Dictionary.get(romanStr[x])
        if x+1 < len(romanStr):
            s2 = Dictionary.get(romanStr[x+1])
            if s1 >= s2:
                result = result+s1
                x = x+1
            else:
                result = result-s1
                x = x+1
        else:
            result = result+s1
            x = x+1
    return result


if __name__ == "__main__":
    romanNumber = input(
        "Podaj poprawna liczbe rzymska(z literami I, V, X, L, C, D, M): ")
    # sprawdzenie czy wpisalismy liczbe rzymska
    for x in romanNumber:
        if x not in Dictionary:
            print("To nie jest poprawna liczba rzymska!!!")
            quit()
    print(roman2int(romanNumber))
