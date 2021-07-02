from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

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

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        res = { "Radius" : self.radius, "Area" : self.calc_area()}
        return res

c = Circle(10)
print(c.toJSON())