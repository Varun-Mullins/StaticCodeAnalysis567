"""
Created on Friday January 24 2020

@author: Varun Mark Mullins
cwid:10456027

This file takes in three lengths of a triangle and checks the validity of the triangle and returns the type of
triangle and checks if it is a right angle triangle or not.

"""


class Triangle:
    """Class for checking the type of triangle"""

    def __init__(self, side_a, side_b, side_c):
        """Initializing the length of the three sides"""
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError("Not a valid Triangle")
        if not self.side_a + self.side_b >= self.side_c and self.side_b + self.side_c >= self.side_a and self.side_a + \
                self.side_c >= self.side_b:
            raise ValueError("Not a valid Triangle")

    def classify_triangle(self):
        """To check if the triangle is equilateral, isosceles or scalene"""
        if self.side_a == self.side_b and self.side_b == self.side_c:
            return "Equilateral Triangle"
        elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_c == self.side_a:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"

    def right_triangle(self):
        """To check if the triangle is a Right angle triangle or not"""

        if self.side_a > self.side_b and self.side_a > self.side_c:
            """Checks for Hypotenuse"""
            if (self.side_a ** 2) == (self.side_b ** 2) + (self.side_c ** 2):
                return "Right angle Triangle"
            else:
                return "Not a Right angle Triangle"
        elif self.side_b > self.side_c and self.side_b > self.side_a:
            """Checks for Hypotenuse"""
            if (self.side_b ** 2) == (self.side_a ** 2) + (self.side_c ** 2):
                return "Right angle Triangle"
            else:
                return "Not a Right angle Triangle"
        elif self.side_c > self.side_a and self.side_c > self.side_b:
            """Checks for Hypotenuse"""
            if (self.side_c ** 2) == (self.side_a ** 2) + (self.side_b ** 2):
                return "Right angle Triangle"
            else:
                return "Not a Right angle Triangle"
