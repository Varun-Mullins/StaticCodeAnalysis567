"""
Created on Friday January 24 2020

@author: Varun Mark Mullins
cwid:10456027

This file tests the three lengths of a triangle provided and tests the validity of the triangle and tests if the file
returns the type of triangle.

"""
import unittest
from HW01_Varun_Mullins import Triangle


class TestFraction(unittest.TestCase):
    """This class checks different conditions of a triangle and checks whether it is a valid triangle or not."""
    def test_init(self):
        """This test checks if all the sides of the triangle get assigned"""
        t = Triangle(1, 2, 3)
        self.assertEqual(t.side_a, 1)
        self.assertEqual(t.side_b, 2)
        self.assertEqual(t.side_c, 3)

    def test_zero(self):
        """Checks whether a side of the triangle is zero or negative"""
        with self.assertRaises(ValueError):
            Triangle(3, 0, 4)
        with self.assertRaises(ValueError):
            Triangle(2, -3, 4)
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

    def test_valid(self):
        """Checks whether the lengths of the triangle provided will for a valid triangle"""
        with self.assertRaises(ValueError):
            Triangle(1, 10, 12)
        with self.assertRaises(ValueError):

            Triangle(2, -3, 4)

    def test_classify_triangle(self):
        """Test for checking the type of triangle"""
        test_t1 = Triangle(3, 3, 3)
        test_t2 = Triangle(3, 4, 4)
        test_t3 = Triangle(3, 4, 5)
        self.assertTrue(test_t1.classify_triangle() == "Equilateral Triangle")
        self.assertTrue(test_t2.classify_triangle() == "Isosceles Triangle")
        self.assertTrue(test_t3.classify_triangle() == "Scalene Triangle")
        self.assertFalse(test_t3.classify_triangle() == "Equilateral Triangle")
        self.assertFalse(test_t1.classify_triangle() == "Scalene Triangle")

    def test_right_triangle(self):
        """Test for checking whether the triangle is a Right angle triangle or not"""
        test_t4 = Triangle(3, 4, 5)
        test_t5 = Triangle(4, 5, 6)
        self.assertTrue(test_t4.right_triangle() == "Right angle Triangle")
        self.assertTrue(test_t5.right_triangle() == "Not a Right angle Triangle")
        self.assertFalse(test_t5.right_triangle() == "Right angle Triangle")


if __name__ == '__main__':
    """ Python assigns __name__ variable as __main__ which can be used when shifting to another module."""
    unittest.main(exit=False, verbosity=2)
