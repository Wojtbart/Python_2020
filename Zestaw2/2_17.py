#2.17
if __name__ == "__main__":

    line = " lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua "
    words=line.split()
    print("Wyrazy posortowane alfabetycznie: ",sorted(words)) # duze litery zawsze sortuje przed malymi
    print("Wyrazy posortowane wzgledem dlugosci", sorted(words, key=len))


