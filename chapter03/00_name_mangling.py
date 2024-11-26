class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

def main():
    p1 = Point()
    # p1.__x = 10

    print(p1.__x)
    print(p1)

if __name__ == "__main__":
    main()
