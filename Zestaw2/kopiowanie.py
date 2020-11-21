import sys
def kopiowanie(inner_file,outer_file ):

    text=""  
    with open(inner_file,"r") as fileRead, open(outer_file,"w") as outFile:

        try:
            for line in fileRead:
                if not line.startswith('#'):
                    text+=line
            outFile.write(text) 
        finally:
            fileRead.close()
            outFile.close()
          
if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("musisz podać nazwy plików!!!!Zamykam")
        sys.exit(1)
    fileIn  = sys.argv[1]
    fileOut = sys.argv[2]    
    kopiowanie(fileIn,fileOut)