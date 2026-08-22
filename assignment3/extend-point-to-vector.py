from math import dist

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self,Point):
        return self.x == Point.x and self.y == Point.y
    
    def __str__(self):
       return f"Point is at x = {self.x}, y = {self.y}"

    def euclidean(self,Point):
        return dist((self.x, self.y), (Point.x, Point.y))
    
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x,y)

    def __str__(self):
        return f"Vector is at x = {self.x}, y = {self.y}"

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)
    
#test
point1 = Point(1,2)
print(point1)
print(point1.euclidean(Point(4,6)))
print(point1 == Point(1,2))

#vector test
vector1 = Vector(1,2)
print(vector1)  
print(vector1 + Vector(4,6))
print(vector1.__add__(Vector(4,6)))
print(vector1.euclidean(Vector(4,6)))
