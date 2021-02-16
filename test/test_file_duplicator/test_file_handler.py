from unittest import TestCase
from file_duplicator.file_handler import FileHandler


class TestIterateFile(TestCase):
    def test_ideal_case(self):
        result = FileHandler.iterate_file('testfile.txt', 1)
        expected = 'testfile(1).txt'
        self.assertEqual(result, expected)

    def test_multiple_periods(self):
        result = FileHandler.iterate_file('test.cfg.xml', 1)
        expected = 'test.cfg(1).xml'
        self.assertEqual(result, expected)


class TestConcatListToString(TestCase):
    def test_only_strings(self):
        result = FileHandler.concat_list_to_string(['this', 'is', 'a', 'test'])
        expected = 'thisisatest'
        self.assertEqual(result, expected)

    def test_with_integers(self):
        result = FileHandler.concat_list_to_string(['this', 1, 'a', 'test'])
        expected = 'this1atest'
        self.assertEqual(result, expected)

