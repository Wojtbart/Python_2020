# 3.4

if __name__ == "__main__":
    while True:
        try:
            x = input("Wpisz jakas liczbe rzeczywista: ")
            if x.lower() != "stop":
                # zaokraglilem do 2 miejsc po przecinku
                print(x, "->", round(pow(float(x), 3), 2))
            elif x.lower() == 'stop':
                break
        except:
            print('Podano napis lub niewlasciwy ciag znakow')
            continue
