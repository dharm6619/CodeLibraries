from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod    
    def calc_area(self):
        pass

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calc_area(self):
        return self.side ** 2 

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        return 3.14 * (self.radius ** 2)

#g = GraphicShape()

c = Circle(7)
s= Square(5)
print(s.calc_area())
print(c.calc_area())