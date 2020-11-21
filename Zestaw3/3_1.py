# 3.1 Czy podany kod jest poprawny składniowo w Pythonie
if __name__ == "__main__":
    x = 2
    y = 3
    if (x > y):
        result = x
    else:
        result = y
    print(result)
# W pythonie nie musimy dodawać ; oraz () w intrukcji warunkowej if, mimo to kod się skompiluje i wukona , składnia podobna do c/c++

    for i in "qwerty":
        if ord(i) < 100:
            print(i)
    # kod nie jest poprawny składniowo, ten if musi się znaleźć w nastepnej linijce
    # literka a ma w ASCII 97,literka d ma 100 itd

    for i in "axby":
        print(ord(i) if ord(i) < 100 else i)
        # print mógłby być w nastepnej linijce, literki a, b i c się nie wyświetlą, gdyż mają numer mniejszy
       # niz 100 w ASCII,kod poprawny
