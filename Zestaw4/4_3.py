# 4.2
def factorial(n):

    temp = 1
    if n >= 0:
        if n == 0:
            return 1
        else:
            for k in range(1, n+1):
                temp = temp*k
            return temp
    else:
        raise Exception("Liczba musi być większa od zera")


if __name__ == "__main__":
    x = 1
    print("Silnia z "+str(x)+" wynosi:", factorial(x))
