from math import dist

class Point:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def equality(self):
        return self.point1 == self.point2
    
    def string_rep(self):
        print(f"point1 is at x1 = {self.point1[0]}, y1 = {self.point1[1]} ")
        print(f"point2 is at x2 = {self.point2[0]}, y2 = {self.point2[1]} ")

    def euclidean(self):
        return dist(self.point1,self.point2)
    
class Vector(Point):
    def __init__(self, vector1, vector2):
        super().__init__(vector1,vector2)

    def string_rep(self):
        print(f"vector1 is at x1 = {self.point1[0]}, y1 = {self.point1[1]} ")
        print(f"vector2 is at x2 = {self.point2[0]}, y2 = {self.point2[1]} ")

    def euclidean(self):
        return (self.point1[0] + self.point2[0],self.point1[1] + self.point2[1])
    
#test
points = Point([1,2],[2,3])
print(points.equality())
points.string_rep()
print(points.euclidean())
print('\n ------------- \n')
vectors = Vector((0,2),(3,0))
vectors.string_rep()
print(vectors.euclidean())
