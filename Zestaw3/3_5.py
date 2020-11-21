# 3.5
def draw(size):
    drawStr = ""
    for x in range(size):
        drawStr += "|"
        for i in range(4):
            drawStr += "."
    drawStr += "|\n"  # dodaje znak nowej linii i ostatnia kreske

    for y in range(size):
        drawStr += str(y)

        if y >= 9 and y < 99:
            for j in range(3):
                drawStr += " "
        elif y >= 99 and y < 999:
            for k in range(2):
                drawStr += " "
        elif y >= 999:
            for l in range(1):
                drawStr += " "
        else:
            for m in range(4):
                drawStr += " "
    # metoda rjust() ważna
    # drawStr += str(y+1)
    # outfile = open('test.txt', 'w')
    # outfile.write(drawStr)
    # outfile.close()

    print(drawStr)


if __name__ == "__main__":
    draw(50)
