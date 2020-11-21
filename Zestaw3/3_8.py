# 3.8

if __name__ == "__main__":
    L1 = "abcdefghijkl12412315678"
    L2 = "agwsfykdsaaa6712312356098765"

    # zrobie je jako zbiory i po prostu wezme z nich przeciecie zbiorow i sume zbiorow
    S1 = set(L1)
    S2 = set(L2)

    print("Elementy wystepujace jednoczesnie w obu sekwencjach (bez powtorzen) to:",
          (" ".join(sorted(S1.intersection(S2)))))
    print("Wszystkie elementy z obu sekwencji (bez powtorzen) to:",
          " ".join(sorted(S1.union(S2))))
