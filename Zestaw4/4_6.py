# 4.6

def sum_seq(sequence):
    sum = 0
    for item in sequence:
        # jezeli nie jest lista ani krotka to dodaje liczby, w przeciwnym wypadku dodawaj wywołania rekurencyjne
        if not isinstance(item, (list, tuple)):
            sum += item
        else:
            sum += sum_seq(item)

    return sum


if __name__ == "__main__":
    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print("Suma sekwencji:", sum_seq(sequence))
