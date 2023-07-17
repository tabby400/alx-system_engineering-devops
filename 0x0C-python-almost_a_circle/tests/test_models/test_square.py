#!/usr/bin/python3
"""Definition for unnitest for rectangle.py"""

import unittest
from models.base import Base
from models.square import Square
import sys
import io

class SquareTest_instance(unittest.TestCase):
    """Using unnitests to test square instances."""

    def test_base(self):
        self.assertIsInstance(Square(9), Base)

    def test_rectangle(self):
        self.assertIsInstance(Square(9), Square)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_1_arg(self):
        sq1 = Square(6)
        sq2 = Square(10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_2_args(self):
        sq1 = Square(12, 4)
        sq2 = Square(4, 12)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_3_args(self):
        sq1 = Square(12, 4, 4)
        sq2 = Square(4, 4, 12)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_4_arg(self):
        self.assertEqual(5, Square(14, 1, 4, 5).id)

    def test_more_than_4_args(self):
        with self.assertRaises(TypeError):
            Square(7, 2, 6, 4, 5)

    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(Square(9, 6, 5, 4).__size)

    def test_getter_size(self):
        self.assertEqual(4, Square(4, 2, 3, 9).size)

    def test_setter_size(self):
        sq = Square(5, 1, 9, 2)
        sq.size = 7
        self.assertEqual(7, sq.size)

    def test_getter_width(self):
        sq = Square(5, 1, 8, 2)
        sq.size = 7
        self.assertEqual(7, sq.width)

    def test_height_get(self):
        sq = Square(4, 1, 8, 2)
        sq.size = 7
        self.assertEqual(7, sq.height)

    def test_x_get(self):
        self.assertEqual(0, Square(9).x)

    def test_y_get(self):
        self.assertEqual(0, Square(9).y)
    
    class Square_Testsize(unittest.TestCase):
    """using unnitest to test size initialization."""

    def test_size_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("wrong")

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.8)

    def test_complexSize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(7))

    def test_size_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"c": 6, "i": 9}, 5)

    def test_boolean_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 5, 7)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([7, 8, 9])

    def test_setter_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({5, 7, 8}, 3)

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((4, 5, 6), 3, 4)

    def test_size_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({5, 6, 7, 1}))

    def test_size_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(7))

    def test_size_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_size_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_size_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_size_Nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_neg_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-7, 2)

    def test_0_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 7)

    class SquareTest_x(unittest.TestCase):
    """Using unnitest to test square x attribute."""

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, "wrong")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, 7.5)

    def test_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, complex(6))

    def test_x_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"t": 4, "f": 3}, 6)

    def test_boolean_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, True)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, [4, 6, 3])

    def test_setter_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {4, 5, 6})

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, (4, 5, 6))

    def test_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({6, 7, 3, 1}))

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(6))

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, b'Python')

    def test_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, bytearray(b'abcdefg'))

    def test_x_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 5)

    def test_x_Nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 4)

    def test_nega_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(7, -8, 0)
    
    class SquareTest_y(unittest.TestCase):
    """sing unnitesst to test square y attribute."""

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 4, None)

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, "wrong")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 4, 5.6)

    def test_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 6, complex(8)

    def test_y_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, {"t": 4, "h": 5})

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, [4, 5, 6])

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {4, 5, 6})

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, (4, 5, 6))

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, frozenset({4, 5, 6, 1}))

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 4, range(7))

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, b'Python')

    def test_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 4, bytearray(b'abcdefg'))

    def test_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 4, memoryview(b'abcedfg'))

    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 1, float('inf'))

    def test_y_Nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 1, float('nan'))

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -8)

    class SquareTest_order_when_initialized(unittest.TestCase):
    """using unnitests to test the order of the square attributes
    when initialized."""

    def test_size_b4_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_b4_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 5, "invalid y")

    def test_x_b4_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "invalid x", "invalid y")

    class SquareTest_area(unittest.TestCase):
    """Using unnitest to test the method area."""

    def test_small_area(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_large_area(self):
        sq = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, sq.area())

    def test_area_diff_attributes(self):
        sq = Square(3, 0, 0, 7)
        sq.size = 8
        self.assertEqual(49, sq.area())

    def test_area_1_arg(self):
        sq = Square(4, 11, 1, 1)
        with self.assertRaises(TypeError):
            sq.area(1)

    class SquareTest_stdout(unittest.TestCase):
    """Using unnitest t test the dispaly method in 
    square class."""

    @staticmethod
    def redirect_stdout(sq, method):
        """returns the txt printed to stdout.

        Arguement:
            sq(square): square to print to stdout.
            method : method to be used on the square
        Returns:
            txt printed to stdout
        """
        output = io.StringIO()
        sys.stdout = stdout
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return (output)

    def test__method_print_str_size(self):
        sq = Square(5)
        output = SquareTest_stdout.redirect_stdout(s, "print")
        expected = "[Square] ({}) 0/0 - 5\n".format(sq.id)
        self.assertEqual(expected, output.getvalue())

    def test_str_x_method_size(self):
        sq = Square(6, 6)
        expected = "[Square] ({}) 6/0 - 6".format(sq.id)
        self.assertEqual(expected, sq.__str__())

    def test_str_method_x_y(self):
        sq = Square(4, 5, 13)
        expected = "[Square] ({}) 5/13 - 4".format(sq.id)
        self.assertEqual(expected, str(sq))

    def test_str_method_x_y_id_size(self):
        sq = Square(3, 33, 5, 12)
        self.assertEqual("[Square] (12) 33/5 - 3", str(sq))

    def test_str_method_diff_attributes(self):
        sq = Square(3, 0, 0, [6])
        sq.size = 12
        sq.x = 7
        sq.y = 9
        self.assertEqual("[Square] ([6]) 7/9 - 12", str(s))

    def test_str_method_1_arg(self):
        sq = Square(4, 2, 3, 4)
        with self.assertRaises(TypeError):
            sq.__str__(1)

    def test_size_display(self):
        sq = Square(2, 0, 0, 7)
        output = SquareTest_stdout.redirect_stdout(sq, "display")
        self.assertEqual("##\n##\n", output.getvalue())

    def test_display_x_size(self):
        sq = Square(3, 1, 0, 15)
        output = TestSquare_stdout.redirect_stdout(sq, "display")
        self.assertEqual(" ###\n ###\n ###\n", output.getvalue())

    def test_display_y_size(self):
        sq = Square(4, 0, 1, 8)
        output = SquareTest_stdout.redirect_stdout(sq, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, output.getvalue())

    def test_display_x_y_size(self):
        sq = Square(2, 4, 2, 1)
        output = TestSquare_stdout.capture_stdout(sq, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, output.getvalue())

    def test_display_1_arg(self):
        sq = Square(4, 5, 6, 2)
        with self.assertRaises(TypeError):
            sq.display(1)

    class SquareTest_args_update(unittest.TestCase):
    """Using unnitest for testing update aaargs method."""

    def test_update_args_0(self):
        sq = Square(9, 9, 9, 9)
        sq.update()
        self.assertEqual("[Square] (9) 9/9 - 9", str(sq))

    def test_update_args1(self):
        sq = Square(9, 9, 9, 9)
        sq.update(69)
        self.assertEqual("[Square] (69) 9/9 - 9", str(sq))

    def test_update_args2(self):
        sq = Square(9, 9, 9, 9)
        sq.update(69, 2)
        self.assertEqual("[Square] (69) 9/9 - 2", str(sq))

    def test_update_args_3(self):
        sq = Square(9, 9, 9, 9)
        sq.update(69, 3, 4)
        self.assertEqual("[Square] (69) 4/9 - 3", str(sq))

    def test_update_args4(self):
        sq = Square(9, 9, 9, 9)
        sq.update(69, 3, 4, 5)
        self.assertEqual("[Square] (69) 4/5 - 3", str(sq))

    def test_update_args_more_than_4(self):
        sq = Square(9, 9, 9, 9)
        sq.update(69, 3, 4, 5, 6)
        self.assertEqual("[Square] (89) 4/5 - 3", str(sq))

    def test_update_args_width_set(self):
        sq = Square(9, 9, 9, 9)
        sq.update(86, 2)
        self.assertEqual(2, sq.width)

    def test_update_args_height_set(self):
        sq = Square(9, 9, 9, 9)
        sq.update(69, 3)
        self.assertEqual(3, sq.height)

    def test_update_None_arg_id(self):
        sq = Square(9, 9, 9, 9)
        sq.update(None)
        expected = "[Square] ({}) 9/9 - 9".format(sq.id)
        self.assertEqual(expected, str(sq))

    def test_update_args_None_id_n_more(self):
        sq = Square(9, 9, 9, 9)
        sq.update(None, 3, 7)
        expected = "[Square] ({}) 7/9 - 3".format(sq.id)
        self.assertEqual(expected, str(sq))

    def test_update_args_two_times(self):
        sq = Square(9, 9, 9, 9)
        sq.update(69, 2, 3, 4)
        sq.update(5, 2, 3, 69)
        self.assertEqual("[Square] (5) 3/69 - 2", str(sq))

    def test_size_update_args_invalid_type(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(69, "invalid")

    def test_update_args_size_0(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(69, 0)

    def test_update_args_neg_size(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(69, -3)

    def test_update_args_x_invalid(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(69, 1, "invalid")

    def test_update_args_x_neg(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(76, 1, -3)

    def test_update_args_y_invalid(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(69, 1, 2, "invalid")

    def test_update_args_y_neg(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(78, 1, 5, -9)

    def test_update_args_size_x_b4(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(76, "invalid", "invalid")

    def test_update_args_size_b4_y(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(99, "invalid", 4, "invalid")

    def test_update_args_x_b4_y(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(99, 1, "invalid", "invalid")

    class SquareTest_update_kwargs(unittest.TestCase):
    """Using unnitests for kwargs update method in square
    class."""

    def test_update_kwargs_1(self):
        sq = Square(9, 9, 9, 9)
        sq.update(id=1)
        self.assertEqual("[Square] (1) 9/9 - 9", str(sq))

    def test_update_kwargs_2(self):
        sq = Square(9, 9, 9, 9)
        sq.update(size=1, id=2)
        self.assertEqual("[Square] (2) 9/9 - 1", str(sq))

    def test_update_kwargs_3(self):
        sq = Square(9, 9, 9, 9)
        sq.update(y=1, size=3, id=69)
        self.assertEqual("[Square] (69) 9/1 - 3", str(sq))

    def test_update_kwargs_4(self):
        sq = Square(9, 9, 9, 9)
        sq.update(id=69, x=1, y=3, size=4)
        self.assertEqual("[Square] (69) 1/3 - 4", str(sq))

    def test_update_kwargs_width_set(self):
        sq = Square(9, 9, 9, 9)
        sq.update(id=69, size=7)
        self.assertEqual(7, sq.width)

    def test_update_kwargs_height_set(self):
        sq = Square(9, 9, 9, 9)
        sq.update(id=79, size=8)
        self.assertEqual(8, sq.height)

    def test_None_update_kwargs_id(self):
        sq = Square(9, 9, 9, 9)
        sq.update(id=None)
        expected = "[Square] ({}) 9/9 - 9".format(sq.id)
        self.assertEqual(expected, str(sq))

    def test_update_kwargs_None_id_n_more(self):
        sq = Square(9, 9, 9, 9)
        sq.update(id=None, size=6, x=12)
        expected = "[Square] ({}) 12/10 - 6".format(sq.id)
        self.assertEqual(expected, str(sq))

    def test_update_kwargs_two_times(self):
        sq = Square(9, 9, 9, 9)
        sq.update(id=87, x=1)
        sq.update(y=3, x=12, size=2)
        self.assertEqual("[Square] (87) 12/3 - 2", str(sq))

    def test_update_kwargs_size_invalid(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size="invalid")

    def test_update_kwargs_size_0(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=0)

    def test_update_kwargs_size_neg(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-5)

    def test_update_kwargs_x_invalid(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x="wrong")

    def test_update_kwargs_x_neg(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-7)

    def test_update_kwargs_y_invalid(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y="wrong")

    def test_update_kwargs_y_neg(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-6)

    def test_update_args_n_kwargs(self):
        sq = Square(9, 9, 9, 9)
        sq.update(87, 2, y=6)
        self.assertEqual("[Square] (87) 9/9 - 2", str(sq))

    def test_update_kwargs_wrong_keys(self):
        sq = Square(9, 9, 9, 9)
        sq.update(u=5, g=10)
        self.assertEqual("[Square] (9) 9/9 - ", str(sq))

    def test_update_kwargs_few_wrong_keys(self):
        sq = Square(9, 9, 9, 9)
        sq.update(size=5, id=99, n=1, i=57)
        self.assertEqual("[Square] (99) 9/9 - 5", str(sq))

    class SquareTest_to_dictionary(unittest.TestCase):
    """using unnitests to test to dictionary method in 
    class square."""

    def test_to_dict_output(self):
        sq= Square(15, 6, 1, 1)
        expected = {'id': 1, 'x': 6, 'size': 15, 'y': 1}
        self.assertDictEqual(expected, sq.to_dictionary())

    def test_to_dictionary_no_obj_change(self):
        sq1 = Square(12, 2, 4, 2)
        sq2 = Square(4, 2, 12)
        sq2.update(**sq1.to_dictionary())
        self.assertNotEqual(sq1, sq2)

    def test_arg_to_dictionary(self):
        sq = Square(9, 9, 9, 9)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
