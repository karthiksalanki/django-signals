class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the Length:"))
    width = int(input("Enter the Width:"))
    rect = Rectangle(length, width)
    for dimension in rect:
        print(dimension)
