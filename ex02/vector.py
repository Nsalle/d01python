class Vector:

    def __init__(self, vect):
        # Dans le cas ou on recoit directement une liste de float
        self.values = []
        if isinstance(vect, list):
            for i in vect:
                if not isinstance(i, float):
                    print("The list can contain only floats")
                    quit()
            self.values = vect
        # Dans le cas ou on recoit juste un int
        elif isinstance(vect, int):
            i = 0.0
            while i < vect:
                self.values.append(i)
                i += 1
        # Dans le cas ou on recoit un tuple
        elif isinstance(vect, tuple):
            if not isinstance(vect[0], int) or not isinstance(vect[1], int):
                print("Range can only contain int")
                quit()
            if (vect[0] > vect[1]):
                i = float(vect[0])
                while (i > vect[1]):
                    self.values.append(i)
                    i -= 1
            else:
                for i in range(*vect):
                    self.values.append(float(i))
        else:
            print("ERROR")
            quit()
        self.size = len(self.values)

    def __add__(self, other):
        try:
            rep = []
            if isinstance(other, Vector):
                i = 0
                while i < len(self.values):
                    rep.append(self.values[i] + other.values[i])
                    i += 1
                return rep
            else:
                i = 0
                while i < len(self.values):
                    rep.append(self.values[i] + other)
                    i += 1
                return rep
        except TypeError:
            print("Wrong type")
            quit()

    def __radd__(self, other):
        try:
            rep = []
            if isinstance(other, Vector):
                i = 0
                while i < len(self.values):
                    rep.append(self.values[i] + other.values[i])
                    i += 1
                return rep
            else:
                i = 0
                while i < len(self.values):
                    rep.append(self.values[i] + other)
                    i += 1
                return rep
        except TypeError:
            print("Wrong type")
            quit()

    def __sub__(self, other):
        try:
            rep = []
            if isinstance(other, Vector):
                i = 0
                while i < len(self.values):
                    rep.append(self.values[i] - other.values[i])
                    i += 1
                return rep
            else:
                i = 0
                while i < len(self.values):
                    rep.append(self.values[i] - other)
                    i += 1
                return rep
        except TypeError:
            print("Wrong type")
            quit()

    def __rsub__(self, other):
        try:
            rep = []
            if isinstance(other, Vector):
                i = 0
                while i < len(self.values):
                    rep.append(other.values[i] - self.values[i])
                    i += 1
                return rep
            else:
                i = 0
                while i < len(self.values):
                    rep.append(other - self.values[i])
                    i += 1
                return rep
        except TypeError:
            print("Wrong type")
            quit()

    def __truediv__(self, other):
        try:
            rep = []
            i = 0
            while i < len(self.values):
                rep.append(self.values[i] / other)
                i += 1
            return rep
        except TypeError:
            print("Wrong type")
            quit()
        except ZeroDivisionError:
            print("Div by 0 Error")

    def __rtruediv__(self, other):
        try:
            rep = []
            i = 0
            while i < len(self.values):
                rep.append(other / self.values[i])
                i += 1
            return rep
        except TypeError:
            print("Wrong type")
            quit()
        except ZeroDivisionError:
            print("Div by 0 Error")

    def __rmul__(self, other):
        try:
            rep = 0
            repv = []
            if isinstance(other, Vector):
                i = 0
                while i < len(self.values):
                    rep += self.values[i] * other.values[i]
                return rep
            else:
                i = 0
                while i < len(self.values):
                    repv.append(self.values[i] * other)
                    i += 1
                return repv
        except TypeError:
            print("Wrong type")
            quit()

    def __mul__(self, other):
        try:
            rep = 0
            repv = []
            if isinstance(other, Vector):
                i = 0
                while i < len(self.values):
                    rep += self.values[i] * other.values[i]
                return rep
            else:
                i = 0
                while i < len(self.values):
                    repv.append(self.values[i] * other)
                    i += 1
                return repv
        except TypeError:
            print("Wrong type")
            quit()

    def __str__(self):
        txt = ""
        txt += "Size = " + str(self.size) + "\n"
        txt += "Vector is : " + str(self.values)
        return txt
