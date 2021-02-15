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
