class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self.number_of_floors

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other


h1 = House('ЖК Республика', 10)
h2 = House('ЖК Санторини', 20)
print(str(h1))
print(str(h2))
print(h1.__eq__(h2))
h1.__add__(10)
print(str(h1))
print(h1.__eq__(h2))

h1.__iadd__(10)
print(str(h1))

h2.__radd__(10)
print(str(h2))

print(h1.__gt__(h2))
print(h1.__ge__(h2))
print(h1.__lt__(h2))
print(h1.__le__(h2))
print(h1.__ne__(h2))
