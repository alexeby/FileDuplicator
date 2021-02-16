import os
import re
from .common import data_handler
from .common.constants import Constants as c
from .api_handler import get_api_data
from .object.object_mapper import ObjectMapper


class FileHandler:

    def __init__(self, api_url, left_token_trim, right_token_trim, num_copies,):
        self.api_url = api_url
        self.left_token_trim = left_token_trim
        self.right_token_trim = right_token_trim
        self.num_copies = num_copies

        self.api_results = None
        self.current_person = None

    @staticmethod
    def get_file_name(file_dir: str):
        files = os.listdir(file_dir)
        if len(files) <= 0:
            raise OSError(f'No files exist in the directory {file_dir}')
        return files[0]

    @staticmethod
    def concat_list_to_string(l: list, delimiter: str = ''):
        result = ''
        for i in l:
            result = result + str(i) + (delimiter if i != l[len(l)-1] else '')
        return result

    @staticmethod
    def get_token_value(token: str, person):
        return data_handler.process(token, person)

    @staticmethod
    def iterate_file(file: str, i: int):
        file_name_list = file.split('.')
        size = len(file_name_list)
        file_type = file_name_list[size-1]
        file_name = FileHandler.concat_list_to_string(file_name_list[0:size-1], '.')
        return file_name + f'({i}).' + file_type

    def set_current_person(self, iteration: int):
        if self.api_results is not None:
            self.current_person = ObjectMapper(self.api_results[iteration]).map_person()

    def conditionally_populate_api_results(self, token: str):
        if self.api_results is None:
            token_upper = token.upper()
            if token_upper.startswith(c.person):
                self.api_results = get_api_data(self.api_url)
                if self.api_results is None:
                    raise Exception('Received no api_results from api_endpoint')
                if len(self.api_results) != self.num_copies:
                    raise Exception(f'num_copies error. Number of api_results={len(self.api_results)} while num_copies={self.num_copies}')
                self.set_current_person(0)

    def parse_line(self, regex_pattern: str, s: str):
        results = re.findall(regex_pattern, s)
        for result in results:
            formatted_result = result.replace(self.left_token_trim, '').replace(self.right_token_trim, '')
            self.conditionally_populate_api_results(formatted_result)
            replace = self.get_token_value(formatted_result, self.current_person)
            s = re.sub(regex_pattern, replace, s, 1)
        return s

    def duplicate_file(self, original_file_dir: str, copy_file_dir: str, num_copies: int, regex_pattern: str):
        original_file_name = self.get_file_name(original_file_dir)
        original_file_path = original_file_dir + original_file_name

        with open(original_file_path, 'r') as original_file:
            for i in range(num_copies):
                self.set_current_person(i)
                copy_file_path = copy_file_dir + self.iterate_file(original_file_name, i + 1)
                with open(copy_file_path, 'w') as copy_file:
                    for line in original_file:
                        parsed_line = self.parse_line(regex_pattern, line)
                        copy_file.write(parsed_line)
                    copy_file.close()
                    original_file.seek(0)
            original_file.close()
