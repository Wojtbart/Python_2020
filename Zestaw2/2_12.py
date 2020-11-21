# 2.12
if __name__ == "__main__":
    line = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
    words = line.split() # przeksztalcam napis na tablice wyrazow
    firstLetters = [word[0] for word in words]
    lastLetters = [word[-1] for word in words]
    print("Napis stworzony z pierwszych znakow:","".join(firstLetters))
    print("Napis stworzony z ostatnich znakow:","".join(lastLetters))


