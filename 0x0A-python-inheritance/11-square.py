#!/usr/bin/python3
'''
    Implementing a Geometry class
'''


class BaseGeometry:
    def area(self):
        '''
            Calculating the area
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            Validating the integer
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
        Implements a rectangle
    '''
    def __init__(self, width, height):
        '''
        Instantiation with width and height: def __init__(self, width, height)
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''
        implement area() method
        '''
        return (self.__width * self.__height)

    def __str__(self):
        '''
        print() should print, and str() should return
        '''
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))


class Square(Rectangle):
    '''
        Implementing the class Square
    '''
    def __init__(self, size):
        '''
        Instantiation with size: def __init__(self, size)
        '''

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''
        implement area() method
        '''
        return(self.__size ** 2)
