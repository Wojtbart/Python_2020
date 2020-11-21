from points import Point
import math


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie.
       Prostokąt jest określony przez podanie dwóch wierzchołków, lewego dolnego i prawego górnego"""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle[{}, {}]".format(self.pt1, self.pt2)

    def __eq__(self, other):  # obsługa rect1 == rect2
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2) or (self.pt1 == other.pt2) and (self.pt2 == other.pt1)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)

    def area(self):            # pole powierzchni
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)
