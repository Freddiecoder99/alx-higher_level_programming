#!/usr/bin/python3
"""
Define a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Parameters:
            - size: a number (float or integer) representing the size of the square (default is 0)
        """
        self.size = size

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
            - value: a number (float or integer) representing the size to set

        Raises:
            - TypeError: if the value is not a number
            - ValueError: if the value is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Checks if the area of this square is equal to the area of another square.

        Parameters:
            - other: a Square object

        Returns:
            True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if the area of this square is not equal to the area of another square.

        Parameters:
            - other: a Square object

        Returns:
            True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of this square is less than the area of another square.

        Parameters:
            - other: a Square object

        Returns:
            True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of this square is less than or equal to the area of another square.

        Parameters:
            - other: a Square object

        Returns:
            True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of this square is greater than the area of another square.

        Parameters:
            - other: a Square object

        Returns:
            True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of this square is greater than or equal to the area of another square.

        Parameters:
            - other: a Square object

        Returns:
            True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

