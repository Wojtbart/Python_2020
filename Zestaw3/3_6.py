# 3.6
def drawRectangle(x, y):
    drawStr = ""
    counter = 0

    for a in range(x+1):

        if counter != x:

            for i in range(y):
                drawStr += "+"
                for j in range(3):
                    drawStr += "-"
            drawStr += "+\n"

            for k in range(y):
                drawStr += "|"
                for l in range(3):
                    drawStr += " "
            drawStr += "|\n"

        else:

            for m in range(y):
                drawStr += "+"
                for n in range(3):
                    drawStr += "-"
            drawStr += "+\n"

        counter = counter+1
    print(drawStr)


if __name__ == "__main__":
    drawRectangle(2, 4)
