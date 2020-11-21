# 3.3 Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3


if __name__ == "__main__":
    for i in range(30):
        if i % 3 != 0:
            print(i)
