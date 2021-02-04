from .generator.number_generator import get_random_num


def number_formatter(x_pattern: str):
    formatted = ''
    for x in x_pattern:
        formatted += str(get_random_num()) if x == 'X' else x
    return formatted
