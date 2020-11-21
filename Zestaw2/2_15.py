#2.15
if __name__ == "__main__":
    L=[1,10,100,1000,10000,356,16,234]
    myString=""
    for digit in L:
        myString+=str(digit)
    print("Zlozony napis to: ",myString)

    #alternatywa
    print("".join(str(x) for x in L))

