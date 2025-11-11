class calculator:
    """Minimum calculator class"""
    def __init__(self, array):
        """Constructor"""
        self.vector = array

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """mul a scalar to each element of the vector."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """sub a scalar to each element of the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """div each element of the vector by scalar."""
        if (object == 0):
            print("Error: Zero divided, not calculate")
            print(self.vector)
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
