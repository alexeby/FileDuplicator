from .generator.number_generator import get_random_num, get_random_num_range
from .generator.date_generator import random_date_generator
from datetime import datetime


def number_formatter(x_pattern: str):
    formatted = ''
    for x in x_pattern:
        formatted += str(get_random_num()) if x == 'X' else x
    return formatted


def date_formatter(date, original_format, changed_format):
    if date is not None and date != '':
        return datetime.strptime(date, original_format).strftime(changed_format)


def generate_date(date_format: str = '%m/%d/%Y', start_date: str = '01/01/1970', end_date: str = 'NOW'):
    return random_date_generator(date_format, start_date, end_date)


def value(values=None):
    if values is None:
        values = []
    return str(values[get_random_num_range(0, len(values) - 1)])


def scramble_string(s=''):
    result = ''
    word_list = [*s]

    for i in range(len(word_list)):
        size = len(word_list)
        n = get_random_num_range(0,size)-1
        result += word_list[n]
        if size > 0:
            word_list.pop(n)

    return result
