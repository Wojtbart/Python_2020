# 4.2

# zadanie3.5-rysowanie miarki

def drawMeasure(size):
    drawStr = ""
    maxSizeSpaces = 5

    for x in range(size):
        drawStr += "|"
        for i in range(4):
            drawStr += "."
    drawStr += "|\n"  # dodaje znak nowej linii i ostatnia kreske

    for y in range(0, size):
        drawStr += str(y)

        spaces = maxSizeSpaces-len(str(y+1))
        # y+1 zeby ostatnia cyfra była w linii kreski
        drawStr += " " * spaces
        # operator * zadziała tu jako mnożenie tzn doda do stringa np 4 spacje

        # if y >= 9 and y < 99:
        #     for j in range(3):
        #         drawStr += " "
        # elif y >= 99 and y < 999:
        #     for k in range(2):
        #         drawStr += " "
        # elif y >= 999:
        #     for l in range(1):
        #         drawStr += " "
        # else:
        #     for m in range(4):
        #         drawStr += " "
    drawStr += str(y+1)
    print(drawStr)


# zadanie3.6-rysowanie prostokąta
def drawRectangle(x, y):
    drawStr = ""
    counter = 0

    for a in range(x+1):  # x+1 żeby rysowało dolna kreske

        for i in range(y):
            drawStr += "+"
            for j in range(3):
                drawStr += "-"
        drawStr += "+\n"

        if counter != x:
            for k in range(y):
                drawStr += "|"
                for l in range(3):
                    drawStr += " "
            drawStr += "|\n"

        counter = counter+1
    print(drawStr)


if __name__ == "__main__":
    drawMeasure(20)
    drawRectangle(3, 5)
