#!/usr/bin/python3

import sys
import unittest
import io
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Using unnitests to test the instances of class
    Rectangle"""

    def test_baseRectangle(self):
        self.assertIsInstance(Rectangle(11, 4), Base)

    def test_rectangle_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(8)

    def test_rectangle_2_args(self):
        rec1 = Rectangle(11, 4)
        rec2 = Rectangle(2, 16)
        self.assertEqual(rec1.id, rec2.id - 1)  # assumes id defined

    def test_rectangle_3_args(self):
        rec1 = Rectangle(4, 2, 1)
        rec2 = Rectangle(3, 2, 7)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_rectangle_4_args(self):
        rec1 = Rectangle(4, 5, 3, 6)
        rec2 = Rectangle(1, 9, 7, 2)
        self.assertEqual(rec1.id, rec2.id - 1)
        
    def test_6_or_more(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 5, 9, 4, 3, 6)

    def test_attribute_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 1, 0, 8).__width)

    def test_attribute_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 1, 0, 8).__height)

    def test_attribute_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 1, 0, 8).__x)

    def test_attribute_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 1, 0, 8).__y)

    def test_attribute_height_setter(self):
        rec = Rectangle(3, 1, 4, 5, 2)
        rec.height = 7
        self.assertEqual(7, rec.height)

    def test_attribute_x_setter(self):
        rec = Rectangle(3, 1, 4, 5, 2)
        rec.x = 7
        self.assertEqual(7, rec.x)

    def test_attribute_y_getter(self):
        rec = Rectangle(3, 1, 4, 5, 2)
        self.assertEqual(5, rec.y)

    def test_attribute_y_setter(self):
        rec = Rectangle(3, 1, 4, 5, 2)
        rec.y = 9
        self.assertEqual(9, rec.y)


class Rectangle_widthTest(unittest.TestCase):
    """Using unnitests when testing width attribute."""

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("wrong", 4)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(4.2, 3)

    def test_width_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(6), 4)

    def test_width_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"b": 6, "c": 7}, 2)

    def test_width_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 4)

    def test_width_lists(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([6, 7, 3], 1)

    def test_width_setter(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({3, 2, 1}, 7)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((5, 2, 1), 5)

    def test_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(6), 4)

    def test_width_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 5)

    def test_width_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 6)

    def test_width_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 5)

    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 9)

    def test_with_Nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 8)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 7)

    def test_width_with_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 8)


class Rectangle_heightTest(unittest.TestCase):
    """Using unnitest in testing the rectangle height."""

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "wrong")

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 3.2)

    def test_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, complex(3))

    def test_height_dictionaty(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"t": 4, "f": 2})

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [3, 7, 3])

    def test_height_setter(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {3, 1, 3})

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (2, 1, 8))

    def test_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, frozenset({2, 1, 8, 6}))

    def test_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_height_bytes(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, b'Python')

    def test_height_bytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, bytearray(b'abcdefg'))

    def test_height_memotyview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def test_height_Nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, float('nan'))

    def test_height_neg(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4)

    def test_height_is_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)


class Rectangle_xTest(unittest.TestCase):
    """Using unnitest for testing the x attribute when initialized."""

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, None)

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 4, "wrong", 1)

    def test_x_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 8, {"a": 5, "b": 6}, 1)

    def test_x_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, True, 4)

    def test_x_width(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, [3, 4, 5], 3)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (3, 2, 1), 5)

    def test_x_frozen(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, frozenset({3, 2, 5, 1}))

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, range(7))

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 2, b'Python')

    def test_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, bytearray(b'abcdefg'))

    def test_memory_view(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 2, memoryview(b'abcedfg'))

    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('inf'), 4)

    def test_x_Nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('nan'), 6)

    def test_x_neg(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(6, 2, -3, 7)


class Rectangle_yTest(unittest.TestCase):
    """Using unnitests when testing the y attribute."""

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 3, None)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 2, "wrong")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 2, 2, 4.5)

    def test_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 2, 1, complex(4))

    def test_y_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 6, 1, {"g": 4, "f": 1})

    def test_y_dictionaty(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 1, [2, 5, 3])

    def test_y_setter(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 4, {4, 5, 6})

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 3, (3, 4, 5))

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({3, 4, 5, 7}))

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 6, range(9))

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 6, 3, b'Python')

    def test_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 3, bytearray(b'abcdefg'))

    def test_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2,  memoryview(b'abcedfg'))

    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 2, 6, float('inf'))

    def test_y_Nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 1, 6, float('nan'))

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(8, 5, 8, -6)


class Rectangle_orderTest(unittest.TestCase):
    """Using unnitest to test the order of rectangle attributes."""

    def test_width_b4_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("wrong width", 8, "wrong x")

    def test_width_be4_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("wrong width", 7, 5, "wrong y")

    def test_height_b4_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, "wrong height", "wrong x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "wrong height", 6, "wrong y")


class Rectangle_areaTest(unittest.TestCase):
    """Using unnitest for testing the area method of rectangle."""

    def test_small_area(self):
        rec = Rectangle(11, 3, 0, 0, 0)
        self.assertEqual(33, rec.area())

    def test_diffAttribures_area(self):
        rec = Rectangle(5, 11, 1, 1, 1)
        rec.width = 6
        rec.height = 10
        self.assertEqual(60, rec.area())

    def test_1_arg_area(self):
        rec = Rectangle(5, 11, 2, 1, 1)
        with self.assertRaises(TypeError):
            rec.area(1)


class Rectangle_outputTest(unittest.TestCase):
    """using unnitest on what will be displayed"""

    @staticmethod
    def redirect_stdout(rec, method):
        """function is used to get the printed txt
        to standard output
        Arguements:
            rec(Rectangle): rectangle to be printed
            method (str): method used in rec
        Returns:
            printed text to the standard output.
        """

        output_buff = io.StringIO()
        sys.stdout = output_buff
        if method == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return (output_buff)

    def test_str_method_width_height_x_y_id(self):
        rec = Rectangle(15, 18, 8, 7, 5)
        self.assertEqual("[Rectangle] (5) 8/7 - 15/18", str(rec))

    def test_diff_attributesStr(self):
        rec = Rectangle(5, 5, 1, 1, [9])
        rec.width = 12
        rec.height = 3
        rec.x = 5
        rec.y = 9
        self.assertEqual("[Rectangle] ([9]) 5/9 - 12/3", str(rec))

    def test_str_1_argMethod(self):
        rec = Rectangle(3, 1, 2, 7, 9)
        with self.assertRaises(TypeError):
            rec.__str__(1)

    def test_display_one_arg(self):
        rec = Rectangle(4, 2, 6, 1, 8)
        with self.assertRaises(TypeError):
            rec.display(1)


class Rectangle_TestUpdate_args(unittest.TestCase):
    """Using unnitest when testing the updating args method."""

    def test_update_args_0(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update()
        self.assertEqual("[Rectangle] (9) 9/9 - 9/9", str(rec))

    def test_update_args_1(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(69)
        self.assertEqual("[Rectangle] (69) 9/9 - 9/9", str(rec))

    def test_update_args_2(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(69, 3)
        self.assertEqual("[Rectangle] (69) 9/9 - 3/9", str(rec))

    def test_update_args_3(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(69, 4, 2)
        self.assertEqual("[Rectangle] (69) 9/9 - 4/2", str(rec))

    def test_update_args_four(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(69, 4, 5, 6)
        self.assertEqual("[Rectangle] (69) 6/9 - 4/5", str(rec))

    def test_update_args_5(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(69, 4, 5, 6, 7)
        self.assertEqual("[Rectangle] (69) 6/7 - 4/5", str(rec))

    def test_more_than_5_update(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(69, 3, 4, 5, 6, 7)
        self.assertEqual("[Rectangle] (69) 5/6 - 3/4", str(rec))

    def test_None_Update_id(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(None)
        expected = "[Rectangle] ({}) 9/9 - 9/9".format(rec.id)
        self.assertEqual(expected, str(rec))

    def test_update_args_id_Noneand_more(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(None, 5, 6, 3)
        expected = "[Rectangle] ({}) 3/9 - 5/6".format(rec.id)
        self.assertEqual(expected, str(rec))

    def test_update_twice_args(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(69, 3, 4, 5, 6, 7)
        rec.update(7, 6, 5, 4, 3, 69)
        self.assertEqual("[Rectangle] (7) 4/3 - 6/5", str(rec))

    def test_update_args_width_invalid_type(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(69, "invalid")

    def test_update_args_width_0(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(69, 0)

    def test_update_args_neg_width_(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(69, -2)

    def test_update_args_height_invalid(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(69, 4, "invalid")

    def test_update_args_height_0(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(69, 2, 0)

    def test_update_args_neg_height(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(67, 2, -5)

    def test_update_args_x_invalid_type(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(69, 2, 8, "invalid")

    def test_update_args_x_negative(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(69, 1, 3, -4)

    def test_update_args_invalid_y(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(69, 3, 4, 5, "invalid")

    def test_update_args_neg_y(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(69, 3, 2, 6, -2)

    def test_update_args_width_be4_height(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(89, "invalid", "invalid")

    def test_update_args_width_b4_x(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(69, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(69, "invalid", 2, 2, "invalid")

    def test_update_args_height_b4_x(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(69, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(69, 2, "invalid", 1, "invalid")

    def test_update_args_x_b4_y(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(69, 1, 2, "invalid", "invalid")


class RectangleTest_update_kwargs(unittest.TestCase):
    """Using unnitest when updating using kwargs."""

    def test_update_kwargs_1(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(id=1)
        self.assertEqual("[Rectangle] (1) 9/9 - 9/9", str(rec))

    def test_update_kwargs_2(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 9/9 - 2/9", str(rec))

    def test_update_kwargs_4(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(id=69, x=1, height=3, y=4, width=5)
        self.assertEqual("[Rectangle] (69) 1/4 - 5/3", str(rec))

    def test_update_kwargs_5(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(y=5, x=7, id=89, width=1, height=3)
        self.assertEqual("[Rectangle] (89) 7/5 - 1/3", str(rec))

    def test_update_kwargs_None_id(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(id=None)
        expected = "[Rectangle] ({}) 9/9 - 9/9".format(rec.id)
        self.assertEqual(expected, str(rec))

    def test_update_kwargs_None_id_with_more(self):
        rec= Rectangle(9, 9, 9, 9, 9)
        rec.update(id=None, height=5, y=8)
        expected = "[Rectangle] ({}) 9/8 - 9/5".format(rec.id)
        self.assertEqual(expected, str(rec))

    def test_update_2wice_kwargs(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(id=69, x=1, height=2)
        rec.update(y=5, height=12, width=2)
        self.assertEqual("[Rectangle] (69) 1/5 - 2/12", str(rec))

    def test_update_invalid_kwargs_width_type(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(width="invalid")

    def test_update_kwargs_width_0(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=0)

    def test_update_kwargs_neg_width(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=-6)

    def test_update_kwargs_height_invalid_type(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(height="invalid")

    def test_update_kwargs_height_0(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=0)

    def test_update_kwargs_neg_height(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=-4)

    def test_update_kwargs_x_invalid_type(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(x="invalid")

    def test_update_kwargs_neg_x(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(x=-6)

    def test_update_kwargs_y_invalid_type(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(y="invalid")

    def test_update_kwargs_y_neg(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(y=-7)

    def test_update_kwargs_args(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(79, 3, height=8, y=6)
        self.assertEqual("[Rectangle] (79) 9/9 - 3/9", str(rec))

    def test_update_kwargs_invalid_keys(self):
        rec = Rectangle(9, 9, 9, 9, 9)
        rec.update(a=5, b=10)
        self.assertEqual("[Rectangle] (9) 9/9 - 9/9", str(rec))


class RectangleTest_to_dictionary(unittest.TestCase):
    """Using unnitest when testing the unnitest method to dictionary."""

    def test_to_dictionary_without_object_changes(self):
        rec1 = Rectangle(11, 2, 1, 9, 7)
        rec2 = Rectangle(7, 9, 1, 2, 11)
        rec2.update(**rec1.to_dictionary())
        self.assertNotEqual(rec1, rec2)

    def test_arg_to_dictionary(self):
        rec = Rectangle(13, 4, 2, 8, 2)
        with self.assertRaises(TypeError):
            rec.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()

