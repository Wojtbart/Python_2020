import unittest
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
            raise ValueError(
                "Błędnie podane wartości, chcemy, aby x1 < x2, y1 < y2!!!")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):      # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"

    def __eq__(self, other):   # obsługa rect1 == rect2
        return ((self.pt1 == other.pt1) and (self.pt2 == other.pt2)) or ((self.pt1 == other.pt2) and (self.pt2 == other.pt1))

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)

    def area(self):            # pole powierzchni
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):   # część wspólna prostokątów
        x1 = max(min(self.pt1.x, self.pt2.x), min(other.pt1.x, other.pt2.x))
        y1 = max(min(self.pt1.y, self.pt2.y), min(other.pt1.y, other.pt2.y))
        x2 = min(max(self.pt1.x, self.pt2.x), max(other.pt1.x, other.pt2.x))
        y2 = min(max(self.pt1.y, self.pt2.y), max(other.pt1.y, other.pt2.y))
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):     # prostąkąt nakrywający oba
        x1 = min(min(self.pt1.x, self.pt2.x), min(other.pt1.x, other.pt2.x))
        y1 = min(min(self.pt1.y, self.pt2.y), min(other.pt1.y, other.pt2.y))
        x2 = max(max(self.pt1.x, self.pt2.x), max(other.pt1.x, other.pt2.x))
        y2 = max(max(self.pt1.y, self.pt2.y), max(other.pt1.y, other.pt2.y))
        return Rectangle(x1, y1, x2, y2)

    # znajdę sobie środek tego prostokąta
    def make4(self):           # zwraca krotkę czterech mniejszych
        center = self.center()
        return [Rectangle(self.pt1.x, self.pt1.y, center.x, center.y), Rectangle(self.pt1.x, center.y, center.x, self.pt2.y), Rectangle(center.x, self.pt1.y, self.pt2.x, center.y), Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)]
