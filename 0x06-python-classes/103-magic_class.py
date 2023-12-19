#!/usr/bin/python3
"""
Define a MagicClass class.
"""

import math

class MagicClass:
    """
    A class that emulates the provided Python bytecode.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass.

        Parameters:
            - radius: a number (float or integer) representing the radius (default is 0)
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            The circumference of the circle.
        """
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    # Example usage
    my_circle = MagicClass(5)
    print("Area:", my_circle.area())
    print("Circumference:", my_circle.circumference())

