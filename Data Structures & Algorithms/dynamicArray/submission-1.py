class DynamicArray:

    def __init__(self, capacity: int):
        self.Array = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.Array[i]

    def set(self, i: int, n: int) -> None:
        self.Array[i] = n

    def pushback(self, n: int) -> None:
        # If array is full, double its capacity
        if self.size == self.capacity:
            self.resize()

        self.Array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.Array[self.size]

    def resize(self) -> None:
        new_array = [0] * (self.capacity * 2)

        # Copy existing elements
        for i in range(self.size):
            new_array[i] = self.Array[i]

        self.Array = new_array
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity