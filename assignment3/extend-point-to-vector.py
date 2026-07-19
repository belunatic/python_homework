from math import dist

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        return self.x == other[0] and self.y == other[1]
    
    def __str__(self):
       return f"Point is at x = {self.x}, y = {self.y}"

    def euclidean(self,other):
        return dist((self.x, self.y), (other.x, other.y))
    
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x,y)

    def __str__(self):
        return f"Vector is at x = {self.x}, y = {self.y}"

    def __add__(self,other):
        return (self.x + other,self.x + other)
    
#test
points = Point(1,2)
points.__eq__((1,2))
print(points)
print(points.euclidean(Point(3,4)))
print('\n ------------- \n')
vectors = Vector((0,2),(3,0))
vectors.__str__()
vectors.__add__((1,1))

