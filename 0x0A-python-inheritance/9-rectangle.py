#!/usr/bin/python3
'''
    Implementing a Geometry class
'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Implements a rectangle
    '''
    def __init__(self, width, height):
        '''
        Instantiation with width and height
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''
        area() method must be implemented
        '''
        return (self.__width * self.__height)

    def __str__(self):
        '''
        return str() and print() should print
        '''
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
