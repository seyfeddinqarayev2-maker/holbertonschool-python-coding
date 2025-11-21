#!/usr/bin/python3
"""This module defines a Square class with printing, getter, and setter."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square with a given size (default 0)."""
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(v
