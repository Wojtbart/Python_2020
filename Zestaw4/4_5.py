# 4.4

# left i right to indeksy listy
def odwracanieIter(L, left, right):

    if right <= len(L) and right >= 0 and left >= 0 and left <= len(L):
        for i in range(len(L)):
            if i >= left and i < right:
                temp = L[i]
                L[i] = L[right]
                L[right] = temp
                right = right-1
            else:
                continue
    else:
        raise Exception("Podano złe zakresy indeksów w liście")
    return L


def odwracanieRek(L, left, right):
    if right <= len(L) and right >= 0 and left >= 0 and left <= len(L):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1
        if left < right:
            odwracanieRek(L, left, right)
    else:
        raise Exception("Podano złe zakresy indeksów w liście")
    return L


if __name__ == "__main__":

    L = [15, 7, 4, 3, 6, 2, 9, 1]
    L2 = [15, 7, 4, 3, 6, 2, 9, 1]

    print("Poczatkowa lista to:", L)
    print("Odwracanie iteracyjne:", odwracanieIter(L, 2, 4))
    print("Odwracanie rekurencyjne:", odwracanieRek(L2, 2, 4))
