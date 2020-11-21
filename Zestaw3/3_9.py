# 3.9
if __name__ == "__main__":
    L = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
    expected_result = [0, 4, 3, 7, 18]

    # l2 też musi być listą
    L2 = [sum(i) for i in L]

    assert L2 == expected_result
    print("Suma:", L2)
