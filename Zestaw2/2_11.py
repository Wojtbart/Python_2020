# 2.11
if __name__ == "__main__":
    word = 'word'
    list_of_letters = ""
    for letter in word:
        if not letter==word[len(word)-1]:
            letter += '_'
        list_of_letters += letter
    print(list_of_letters)

   #alternatywa i najlepszy sposób
    print("_".join(word))

