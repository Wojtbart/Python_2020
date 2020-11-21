# 2.13
if __name__ == "__main__":

    line = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
    words = line.split() # przeksztalcam napis na tablice wyrazow
    list1 = [] # lista z dlugoscia poszczegolnych wyrazow
    for word in words:
        list1.append(len(word))
    print("laczna długosc napisow w wyrazie line to:", sum(list1))
    
    #alternatywa i najlepszy sposób
    print(sum(len(words) for words in line.split()))

