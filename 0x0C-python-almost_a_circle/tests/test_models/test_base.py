#!/usr/bin/python3

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import os

class BaseTest(unittest.TestCase):
    """Using unnitests to test instances of the base class."""

    def test_not_arg(self):
        bs1 = Base()
        bs2 = Base()
        self.assertEqual(bs1.id, bs2.id - 1)

    def test_3_bases(self):
        bs1 = Base()
        bs2 = Base()
        bs3 = Base()
        self.assertEqual(bs1.id, bs3.id - 2)

    def test_id_None(self):
        bs1 = Base(None)
        bs2 = Base(None)
        self.assertEqual(bs1.id, bs2.id - 1)

    def test_id_unique(self):
        self.assertEqual(11, Base(11).id)

    def test_nb_inst_aft_unique_id(self):
        bs1 = Base()
        bs2 = Base(11)
        bs3 = Base()
        self.assertEqual(bs1.id, bs3.id - 1)

    def test_public_id(self):
        bs = Base(11)
        bs.id = 14
        self.assertEqual(14, bs.id)

    def test_nb_inst_private(self):
        with self.assertRaises(AttributeError):
            print(Base(11).__nb_instances)

    def test_id_str(self):
        self.assertEqual("why", Base("why").id)

    def test_id_float(self):
        self.assertEqual(3.2, Base(3.2).id)

    def test_id_complex(self):
        self.assertEqual(complex(4), Base(complex(4)).id)

    def test_id_dictionary(self):
        self.assertEqual({"x": 4, "p": 2}, Base({"x": 4, "p": 2}).id)

    def test_boolean_id(self):
        self.assertEqual(True, Base(True).id)

    def test_id_list(self):
        self.assertEqual([4, 5, 3], Base([4, 5, 3]).id)

    def test_id_tuple(self):
        self.assertEqual((3, 2), Base((3, 2)).id)

    def test_setter_id(self):
        self.assertEqual({6, 2, 9}, Base({6, 2, 9}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({4, 5, 6}), Base(frozenset({4, 5, 6})).id)

    def test_id_range(self):
        self.assertEqual(range(7), Base(range(7)).id)

    def test_id_bytes(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_id_bytearray(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_id_memoryview(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_id_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_id_Nan(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_2_args(self):
        with self.assertRaises(TypeError):
            Base(4, 5)

    class BaseTest_to_json_string(unittest.TestCase):
        """Using unnitests for tests when it comes to json
    string method"""

    def test_empty_list_to_json_string(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none_to_json_string(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args_to_json_string(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arg_to_json_string(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_rectangle_to_json_string_type(self):
        rect = Rectangle(14, 32, 2, 5)
        self.assertEqual(str, type(Rectangle.to_json_string([rect.to_dictionary()])))

    def test_rectangle_to_json_string_one_dict(self):
        rect = Rectangle(13, 2, 5, 1, 8)
        self.assertTrue(len(Rectangle.to_json_string([rect.to_dictionary()])) == 46)

    def test_rectangle_to_json_string_two_dicts(self):
        rect1 = Rectangle(2, 3, 5, 19, 2)
        rect2 = Rectangle(4, 2, 4, 1, 12)
        list_dictionary = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Rectangle.to_json_string(list_dictionary)) == 78)

    def test_square_to_json_string_type(self):
        square = Square(10, 4, 3, 9)
        self.assertEqual(str, type(Square.to_json_string([square.to_dictionary()])))

    def test_square_to_json_string_one_dict(self):
        square = Square(10, 4, 3, 9)
        self.assertTrue(len(Square.to_json_string([square.to_dictionary()])) == 69)

    def test_square_to_json_string_two_dicts(self):
        square1 = Square(10, 4, 3, 9)
        square2 = Square(4, 6, 20, 2)
        list_dictionary = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertTrue(len(Square.to_json_string(list_dictionary)) == 118)

    class BaseTest_saveto_file(unittest.TestCase):
        """Using unnitests to test method save to file
    in base"""

    @classmethod
    def tearDown(self):
        """Deletion of created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_1_rectangle(self):
        rec = Rectangle(9, 3, 2, 4, 5)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as fh:
            self.assertTrue(len(fh.read()) == 60)

    def test_save_to_file_2_rectangles(self):
        rec1 = Rectangle(9, 3, 2, 4, 5)
        rec2 = Rectangle(8, 4, 4, 6, 3)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as fh:
            self.assertTrue(len(fh.read()) == 115)

    def test_save_to_file_1_square(self):
        sq = Square(13, 4, 2, 9)
        Square.save_to_file([sq])
        with open("Square.json", "r") as fh:
            self.assertTrue(len(fh.read()) == 43)

    def test_save_to_file_two_squares(self):
        sq1 = Square(11, 6, 2, 7)
        sq2 = Square(3, 8, 2, 3)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as fh:
            self.assertTrue(len(fh.read()) == 87)

    def test_save_to_file_class_nm_for_filename(self):
        sq = Square(5, 2, 7, 8)
        Base.save_to_file([sq])
        with open("Base.json", "r") as fh:
            self.assertTrue(len(fh.read()) == 49)

    def test_save_to_file_overwrite(self):
        sq = Square(7, 3, 29, 9)
        Square.save_to_file([sq])
        sq = Square(15, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as fh:
            self.assertTrue(len(fh.read()) == 40)

    def test_None_save_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as fh:
            self.assertEqual("[]", fh.read())

    def test_emptyl_save_to_file(self):
        Square.save_to_file([])
        with open("Square.json", "r") as fh:
            self.assertEqual("[]", fh.read())

    def test_save_to_file_not_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
    
    class BaseTest_from_json(unittest.TestCase):
        """Using unnitests when testing from json string method in base 
    class."""

    def test_type_from_json_string(self):
        list_in = [{"id": 99, "width": 11, "height": 3}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list, type(list_out))

    def test_from_json_string_1_rectangle(self):
        list_in = [{"id": 99, "width": 11, "height": 3, "x": 4}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_2_rectangles(self):
        list_in = [
            {"id": 99, "width": 11, "height": 3, "x": 7, "y": 7},
            {"id": 78, "width": 9, "height": 1, "x": 4, "y": 2},
        ]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_1_square(self):
        list_in = [{"id": 99, "size": 11, "height": 5}]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_2_squares(self):
        list_in = [
            {"id": 99, "size": 11, "height": 5},
            {"id": 7, "size": 8, "height": 5}
        ]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_None_from_json_string(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_list_from_json_string(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_not_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    class BaseTest_create(unittest.TestCase):
        """Using unnitest for testing method create of base class."""

    def test_create_rectangle(self):
        rec1 = Rectangle(3, 6, 6, 2, 1)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (1) 2/2 - 3/6", str(rec1))

    def test_new_create_rectangle(self):
        rec1 = Rectangle(3, 6, 7, 1, 8)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (8) 1/1 - 6/3", str(rec2))

    def test_to_create_rectangle(self):
        rec1 = Rectangle(3, 6, 7, 1, 8)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertIsNot(rec1, rec2)

    def test_create_equal_rectangle(self):
        rec1 = Rectangle(3, 6, 4, 2, 8)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertNotEqual(rec1, rec2)

    def test_create_square_(self):
        sq1 = Square(4, 5, 3, 8)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (8) 3/3 - 4", str(sq1))

    def test_new_create_square(self):
        sq1 = Square(4, 5, 3, 8)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (8) 3/3 - 4", str(sq2))

    def test_to_create_square(self):
        sq1 = Square(4, 5, 3, 8)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertIsNot(sq1, sq2)

    def test_equal_create_square(self):
        sq1 = Square(4, 5, 3, 8)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertNotEqual(sq1, sq2)


    class BaseTest_load_fromFile(unittest.TestCase):
        """Using unnitest to test load from file from base."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_rectangle1_load_from_file_(self):
        rec1 = Rectangle(12, 4, 1, 5, 3)
        rec2 = Rectangle(4, 5, 7, 9, 2)
        Rectangle.save_to_file([rec1, rec2])
        list_rect_out = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(list_rect_out[0]))

    def test_load_from_file_2_rectangle(self):
        rec1 = Rectangle(12, 4, 1, 5, 1)
        rec2 = Rectangle(9, 3, 4, 9, 2)
        Rectangle.save_to_file([rec1, rec2])
        list_rect_out = Rectangle.load_from_file()
        self.assertEqual(str(rec2), str(list_rect_out[1]))

    def test_types_load_from_file_rectangle(self):
        rec1 = Rectangle(12, 4, 1, 5, 2)
        rec2 = Rectangle(9, 3, 4, 9, 7)
        Rectangle.save_to_file([rec1, rec2])
        out = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in out))

    def test_load_from_file_square1(self):
        sq1 = Square(4, 2, 3, 9)
        sq2 = Square(8, 6, 1, 7)
        Square.save_to_file([sq1, sq2])
        list_sq_out = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_sq_out[0]))

    def test_load_from_file_2_square(self):
        sq1 = Square(6, 4, 2, 5 )
        sq2 = Square(7, 3, 1, 9)
        Square.save_to_file([sq1, sq2])
        list_sq_out = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_sq_out[1]))

    def test_types_load_from_file_square(self):
        sq1 = Square(6, 1, 4, 5)
        sq2 = Square(8, 9, 1, 3)
        Square.save_to_file([sq1, sq2])
        out = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in out))

    def test_load_from_file_not_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    class BaseTest_save_to_filecsv(unittest.TestCase):
        """Using unnitest to testsave to file csv method
    in base class."""

    @classmethod
    def tearDown(self):
        """Deletion of created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_1_rectangle(self):
        rec = Rectangle(10, 8, 3, 7, 4)
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", "r") as fh:
            self.assertTrue("4,10,8,3,7", fh.read())

    def test_save_to_file_csv_2_rectangles(self):
        rec1 = Rectangle(10, 8, 1, 8, 4)
        rec2 = Rectangle(9, 4, 7, 3, 6)
        Rectangle.save_to_file_csv([rec1, rec2])
        with open("Rectangle.csv", "r") as fh:
            self.assertTrue("4,10,8,1,8\n9,4,7,3,6", fh.read())

    def test_save_to_file_csv_1_square(self):
        sq = Square(13, 6, 2, 7)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as fh:
            self.assertTrue("7,13,6,2", fh.read())

    def test_save_to_file_csv_2_squares(self):
        sq1 = Square(11, 6, 1, 7)
        sq2 = Square(7, 6, 2, 5)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "r") as fh:
            self.assertTrue("7,11,6,1\n5,7,6,2", fh.read())

    def test_save_to_file__csv_class_nme(self):
        sq = Square(12, 8, 3, 9)
        Base.save_to_file_csv([sq])
        with open("Base.csv", "r") as fh:
            self.assertTrue("9,12,8,3", fh.read())

    def test_csv_save_to_file_overwrite(self):
        sq = Square(7, 8, 13, 1)
        Square.save_to_file_csv([sq])
        sq = Square(11, 6, 4, 7)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as fh:
            self.assertTrue("7,11,6,4", fh.read())

    def test_None_save_to_file__csv(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as fh:
            self.assertEqual("[]", fh.read())

    def test_save_to_file_csv_empty_l(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as fh:
            self.assertEqual("[]", fh.read())

    def test_save_to_file_csv_not_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


