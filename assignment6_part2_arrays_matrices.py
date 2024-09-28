class Array:
    def __init__(self, size):
        # Initialize the Array with a specified size, filling it with None
        self.size = size
        self.array = [None] * size

    def insert(self, index, value):
        # Insert a value at a specific index if it's within bounds
        if index >= 0 and index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds.")

    def delete(self, index):
        # Set the value at the specified index to None (deleting the value)
        if index >= 0 and index < self.size:
            self.array[index] = None
        else:
            raise IndexError("Index out of bounds.")

    def access(self, index):
        # Retrieve the value at the specified index if it's within bounds
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds.")

# Matrix Operations (2D Arrays)


class Matrix:
    def __init__(self, rows, cols):
        # Initialize a Matrix with given rows and columns, filling with None
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        # Insert a value at the specified row and column if within bounds
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            self.matrix[row][col] = value
        else:
            raise IndexError("Index out of bounds.")

    def delete(self, row, col):
        # Set the value at the specified row and column to None (deleting the value)
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            self.matrix[row][col] = None
        else:
            raise IndexError("Index out of bounds.")

    def access(self, row, col):
        # Retrieve the value at the specified row and column if within bounds
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            return self.matrix[row][col]
        else:
            raise IndexError("Index out of bounds.")
