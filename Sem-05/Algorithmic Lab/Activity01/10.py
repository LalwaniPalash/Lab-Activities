class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def sort_points_by_x(points):
    """
    Sort a list of Point objects based on their x-coordinate.
    
    :param points: List of Point objects
    :return: A new list of Point objects sorted by x-coordinate
    """
    return sorted(points, key=lambda point: point.x)

if __name__ == "__main__":
    points = [Point(3, 4), Point(1, 2), Point(5, 6), Point(2, 1)]
    
    sorted_points = sort_points_by_x(points)
    
    print("Points sorted by x-coordinate:", sorted_points)
