# 4.4
def fibonacci(n):
    a = 0
    b = 1

    if n >= 0:
        for i in range(0, n):
            result = a+b
            a = b
            b = result

        return a
    else:
        raise Exception("Liczba musi być większa od zera")
# iteracyjna dużo lepsza


def fibonacciRec(n):
    if n >= 0:
        if n == 0 or n == 1:
            return n
        else:
            return fibonacciRec(n-2)+fibonacciRec(n-1)
    else:
        raise Exception("Liczba musi być większa od zera")


if __name__ == "__main__":
    x = 9
    print(str(x)+"-ty wyraz ciagu Fibonacciego iteracyjnie wynosi:", fibonacci(x))
    print(str(x)+"-ty wyraz ciagu Fibonacciego rekurecyjnie wynosi:", fibonacciRec(x))
