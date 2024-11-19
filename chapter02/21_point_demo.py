import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2)) 


def main():
    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(p1.distance_to(p2))

    p1.x = 15
    p1.y = 15
    print(p1.distance_to(p2))

    print(f"Point p1: {p1}")
    print(p2)


if __name__ == "__main__":
    main()