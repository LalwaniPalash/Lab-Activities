class Point:
    x = 0
    y = 0

    def movePoint(self, newX, newY):
    	self.x = newX
    	self.y = newY

    def get_coordinates(self):
    	return self.x, self.y

point1 = Point()
point2 = Point()

point1.movePoint(5, 3)

print("Coordinates of point1:", point1.get_coordinates())
print("Coordinates of point2:", point2.get_coordinates())
