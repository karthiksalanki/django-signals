class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        # Initialize the iterator index
        self._index = 0

    def __iter__(self):
        # Return the iterator object, which is self in this case
        self._index = 0  # Reset index for fresh iteration
        return self

    def __next__(self):
        # Implement the logic for iteration

        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            # Stop iteration when both length and width are returned
            raise StopIteration

# Example Usage
length = int(input('Length: '))
width = int(input('Width: '))
rectangle = Rectangle(length, width)

for dimension in rectangle:
    print(dimension)
