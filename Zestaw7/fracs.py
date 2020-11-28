class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError("Mianownik jest równy zero!!!")
        elif isinstance(x, float) or isinstance(y, float):
            if isinstance(x, float) and isinstance(y, float):
                self.x = x.as_integer_ratio()[0]*y.as_integer_ratio()[1]
                self.y = y.as_integer_ratio()[0]*x.as_integer_ratio()[1]
            elif isinstance(x, float) and isinstance(y, int):
                self.x = x.as_integer_ratio()[0]
                self.y = x.as_integer_ratio()[1]*y
            else:
                self.x = y.as_integer_ratio()[1]*x
                self.y = y.as_integer_ratio()[0]
        else:
            self.x = x
            self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{}".format(self.x)
        else:
            return str(self.x) + "/" + str(self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    # Python 2
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3

    def __eq__(self, other):
        if isinstance(other, Frac):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            raise ValueError("Bląd w porównywaniu, drugi argument to: "+other)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    # def __gt__(self, other): pass

    # def __ge__(self, other): pass

    def __add__(self, other):   # frac1+frac2, frac+int
        if isinstance(other, Frac):
            return Frac(self.x * other.y + self.y * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x + (other*self.y), self.y)
        else:
            raise ValueError("Blad w dodawaniu ulamkow")

    __radd__ = __add__              # int+frac

    def __sub__(self, other):   # frac1-frac2, frac-int
        if isinstance(other, Frac):
            return Frac(self.x * other.y - self.y * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x - (other*self.y), self.y)
        else:
            raise ValueError("Blad w odejmowaniu ulamkow")

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):   # frac1*frac2, frac*int
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x * other, self.y)
        else:
            raise ValueError("Blad w mnozeniu ulamkow")

    __rmul__ = __mul__              # int*frac

    # def __div__(self, other):   # frac1/frac2, frac/int, Python 2

   # def __rdiv__(self, other): pass  # int/frac, Python 2

    def __truediv__(self, other):   # frac1/frac2, frac/int, Python 3
        if isinstance(other, Frac):
            if other.x == 0 or other.y == 0:
                raise ValueError("Dolny ułamek jest równy zero, nie wolno!!!!")
            else:
                return Frac(self.x * other.y, self.y * other.x)
        elif isinstance(other, int):
            if other == 0:
                raise ValueError("Nie mozna dzielić przez zero!!!!")
            else:
                return Frac(self.x, self.y * other)
        else:
            raise ValueError("Blad w dzieleniu ulamkow")

    def __rtruediv__(self, other):   # int/frac, Python 3
        if isinstance(other, int):
            return Frac(self.y*other, self.x)
        else:
            raise ValueError("Blad w dzieleniu ulamkow")

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac((-1)*self.x, self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):      # float(frac)
        return self.x/self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])
