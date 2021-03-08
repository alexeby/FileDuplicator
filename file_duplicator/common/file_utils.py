from .data_handler import process
import os


def get_file_name(file_dir: str):
    files = os.listdir(file_dir)
    if len(files) <= 0:
        raise OSError(f'No files exist in the directory {file_dir}')
    return files[0]


def concat_list_to_string(l: list, delimiter: str = ''):
    result = ''
    for i in l:
        result = result + str(i) + (delimiter if i != l[len(l)-1] else '')
    return result


def get_token_value(token: str, person):
    return process(token, person)


def iterate_file(file: str, i: int):
    file_name_list = file.split('.')
    size = len(file_name_list)
    file_type = file_name_list[size-1]
    file_name = concat_list_to_string(file_name_list[0:size-1], '.')
    return file_name + f'_{i}.' + file_type
