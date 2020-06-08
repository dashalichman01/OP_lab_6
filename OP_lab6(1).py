from abc import ABC, abstractmethod
class Polyhedrons(ABC):
    def __init__(self,side):
        self.side = side
    @abstractmethod
    def calculate_square(self):
        return self.side ** 2
    @abstractmethod
    def calculate_volume(self):
        return self.side ** 3
class Tetrahedron(Polyhedrons):
    def __init__(self,side):
        super().__init__(side)
    def calculate_square(self):
        square = (self.side)**2 * (3 ** (1 / 3))
        return square
    def calculate_volume(self):
        volume = ((self.side)**3)/12*(2 ** (1 / 2))
        return volume
class Cube(Polyhedrons):
    def __init__(self,side):
        super().__init__(side)
    def calculate_square(self):
        super().calculate_square()
        square = (self.side)**2 * 6
        return square
    def calculate_volume(self):
        volume = ((self.side)**3)
        return volume
class Octahedron(Polyhedrons):
    def __init__(self,side):
        super().__init__(side)
    def calculate_square(self):
        square = 2 * (self.side) ** 2 * (3 ** (1/3))
        return square
    def calculate_volume(self):
        volume = ((self.side) ** 3) / 3 * (2 ** (1/2))
        return volume
kub = Cube(2)
