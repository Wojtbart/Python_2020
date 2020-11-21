#2.14
if __name__ == "__main__":
    line = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
    words = line.split() # przeksztalcam napis na tablice wyrazow
    list1 = [] # lista z dlugoscia poszczegolnych wyrazow
    for word in words:
        list1.append(len(word))

    findWord="" #szukane slowo
    for word in words:
        if(len(word)== max(list1)):
            findWord=word
    print ("Dlugosc najdluszego wyrazu to:", max(list1))
    print ("Najdluszy wyraz to:", findWord)

    #najdluzszy napis i jego dlugosc- alternatywa
    print(max(line.split(), key=len))
    print(len(max(line.split(), key=len)))


