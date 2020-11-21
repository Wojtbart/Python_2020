# 4.7
def flatten(sequence):
    flattenList = []
    for item in sequence:
        # jezeli nie jest lista ani krotka to dodaje jako elemnty do listy, w przeciwnym wypadku dodawaj wywołania rekurencyjne
        if not isinstance(item, (list, tuple)):
            flattenList.append(item)
        else:
            flattenList += (flatten(item))

    return flattenList


if __name__ == "__main__":
    seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    assert flatten(seq) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(flatten(seq))            # [1,2,3,4,5,6,7,8,9]
