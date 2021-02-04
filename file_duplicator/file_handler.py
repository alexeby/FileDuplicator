import os
import re
from .common import data_handler
from .api_handler import get_api_data
from .object.object_mapper import ObjectMapper


def get_file_name(file_dir: str):
    files = os.listdir(file_dir)
    if len(files) <= 0:
        raise OSError(f'No files exist in the directory {file_dir}')
    return files[0]


def concat_list_to_string(l: list, delimiter: str = ''):
    result = ''
    for i in l:
        result = result + i + (delimiter if i != l[len(l)-1] else '')
    return result


def iterate_file(file: str, i: int):
    file_name_list = file.split('.')
    size = len(file_name_list)
    file_type = file_name_list[size-1]
    file_name = concat_list_to_string(file_name_list[0:size-1], '.')
    return file_name + f'({i}).' + file_type


def get_token_value(token: str, person):
    return data_handler.process(token, person)


def parse_line(regex_pattern: str, s: str, person):
    results = re.findall(regex_pattern, s)
    for result in results:
        formatted_result = result.replace('{', '').replace('}', '')
        replace = get_token_value(formatted_result, person)
        s = re.sub(regex_pattern, replace, s, 1)
    return s


def duplicate_file(original_file_dir: str, copy_file_dir: str, num_copies: int, regex_pattern: str, api_url: str):
    original_file_name = get_file_name(original_file_dir)
    original_file_path = original_file_dir + original_file_name
    api_results = get_api_data(api_url)

    with open(original_file_path, 'r') as original_file:
        for i in range(num_copies):
            person = ObjectMapper(api_results[i]).map_person()
            copy_file_path = copy_file_dir + iterate_file(original_file_name, i + 1)
            with open(copy_file_path, 'w') as copy_file:
                for line in original_file:
                    parsed_line = parse_line(regex_pattern, line, person)
                    copy_file.write(parsed_line)
                copy_file.close()
                original_file.seek(0)
        original_file.close()
