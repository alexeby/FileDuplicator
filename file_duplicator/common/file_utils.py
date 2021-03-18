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


def iterate_file(file: str, i: int):
    file_name_list = file.split('.')
    size = len(file_name_list)
    file_type = file_name_list[size-1]
    file_name = concat_list_to_string(file_name_list[0:size-1], '.')
    return file_name + f'_{i}.' + file_type


def parse_string_for_token(s: str, left_token: str, right_token: str):
    left_token_index = s.rfind(left_token)
    right_token_index = s.find(right_token, left_token_index)

    if right_token_index == -1 and left_token_index == -1:
        return None

    token = s[left_token_index:right_token_index + len(right_token)]
    return token


def get_key(val, dictionary: dict):
    for key, v in dictionary.items():
        if val in v:
            return key
    return ''
