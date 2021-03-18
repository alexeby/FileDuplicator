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


class TestParseStringForToken(TestCase):
    def test_no_tokens(self):
        result = file_utils.parse_string_for_token('My name is Person One', '{', '}')
        self.assertIsNone(result)

    def test_one_token(self):
        result = file_utils.parse_string_for_token('My name is {FirstName} One', '{', '}')
        expected = '{FirstName}'
        self.assertEqual(result, expected)

    def test_two_tokens(self):
        result = file_utils.parse_string_for_token('My name is {FirstName} {LastName}', '{', '}')
        expected = '{LastName}'
        self.assertEqual(result, expected)

    def test_nested_tokens(self):
        result = file_utils.parse_string_for_token('My name is {FirstName{MiddleName} nice to meet you}', '{', '}')
        expected = '{MiddleName}'
        self.assertEqual(result, expected)

    def test_empty_token(self):
        result = file_utils.parse_string_for_token('My name is {FirstName{Middle{}Name} nice to meet you}', '{', '}')
        expected = '{}'
        self.assertEqual(result, expected)