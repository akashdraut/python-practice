import math


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * math.pow(self.radius, 2)
        return area
    
    def calcualte_circumferance(self):
        circumferance = 2 * 3.14 * self.radius
        return circumferance
    

result = Circle(5)
print(result.calculate_area())
print(result.calcualte_circumferance())





