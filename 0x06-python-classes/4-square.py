#!/usr/bin/python3
"""Describe a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Start a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Find/set the new size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size should be an int")
        elif value < 0:
            raise ValueError("size shuold be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
