#!/usr/bin/python3
"""
Contains a definition for class rectangle.
"""


class Rectangle:
    """Definition of class rectangle.

       Attributes:
           width(int): rectangle width.
           height(int): rectangle height.
    """
    def __init__(self, width=0, height=0):
        """
            Initializes a new Class Rectangle instance.
            
            Args:
                width(int): rectangle width.
                height(int): rectangle height.

                Raises:
                TypeError: if width/height is not int.
