from unittest import TestCase
from file_duplicator.common import file_utils


class TestIterateFile(TestCase):
    def test_ideal_case(self):
        result = file_utils.iterate_file('testfile.txt', 1)
        expected = 'testfile_1.txt'
        self.assertEqual(result, expected)

    def test_multiple_periods(self):
        result = file_utils.iterate_file('test.cfg.xml', 1)
        expected = 'test.cfg_1.xml'
        self.assertEqual(result, expected)


class TestConcatListToString(TestCase):
    def test_only_strings(self):
        result = file_utils.concat_list_to_string(['this', 'is', 'a', 'test'])
        expected = 'thisisatest'
        self.assertEqual(result, expected)

    def test_with_integers(self):
        result = file_utils.concat_list_to_string(['this', 1, 'a', 'test'])
        expected = 'this1atest'
        self.assertEqual(result, expected)

