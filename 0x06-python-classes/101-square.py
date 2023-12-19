#!/usr/bin/python3
"""
Define a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Parameters:
            - size: an integer representing the size of the square (default is 0)
            - position: a tuple of 2 positive integers representing the position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
            - value: an integer representing the size to set

        Raises:
            - TypeError: if the value is not an integer
            - ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            The position of the square as a tuple of 2 positive integers.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
            - value: a tuple of 2 positive integers representing the position to set

        Raises:
            - TypeError: if the value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square using the character '#' in stdout.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    my_square.my_print()

    print("--")

    my_square = Square(5, (4, 1))
    my_square.my_print()

