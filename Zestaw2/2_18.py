#2.18
if __name__ == "__main__":
    
    bigNUmber=1000000000000000
    bigNumberStr=str(bigNUmber)
    counter=0
    for digit in bigNumberStr:
        if(digit=='0'):
            counter=counter+1
    print("Liczba zer w liczbie to: "+str(counter))

    #test na istnienie zera
    any(x=='0' for x in str(bigNUmber))