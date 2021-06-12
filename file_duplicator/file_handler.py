import sys
import logging
from datetime import datetime
from .object.object_mapper import ObjectMapper
from .exception.exception import InvalidTokenException
from .common import data_handler
from .common import file_utils
from .api_handler import get_api_data
from .common.constants import Constants as c
from .setup.mappings import Mappings as m


logger = logging.getLogger(__name__)


class FileHandler:

    def __init__(self, api_url, left_token_trim, right_token_trim, num_copies, unique_person_keys, all_unique_persons,
                 num_records_per_file, mapping_tokens):
        self.api_url = api_url
        self.left_token_trim = left_token_trim
        self.right_token_trim = right_token_trim
        self.num_copies = num_copies
        self.unique_person_keys: set = unique_person_keys
        self.all_unique_persons = all_unique_persons
        self.num_records_per_file = len(unique_person_keys) if len(unique_person_keys) > 0 else num_records_per_file
        self.mapping_tokens = dict.fromkeys(mapping_tokens, 0)
        c.iterator = 0

        self.person_list = self.populate_person_list()
        self.unique_person_map = self.populate_multiple_person_map() if self.all_unique_persons.upper() != 'TRUE' \
            else self.populate_all_unique_map()

    def populate_person_list(self):
        person_list = []
        number_persons = self.num_records_per_file * self.num_copies
        if number_persons > 0:
            api_results: list = get_api_data(self.api_url + str(number_persons))
            for result in api_results:
                person_list.append(ObjectMapper(result).map_person())
        return person_list

    def populate_multiple_person_map(self):
        person_list = self.person_list
        unique_person_map = {k: [] for k in self.unique_person_keys}
        i = 0
        while i < len(person_list):
            for key in self.unique_person_keys:
                unique_person_map[key].append(i)
                i += 1
        return unique_person_map

    def populate_all_unique_map(self):
        number_persons = self.num_records_per_file * self.num_copies
        mapping_list = []
        i = 0
        while i < number_persons:
            iter_list = []
            for j in range(self.num_copies):
                iter_list.append(i)
                i += 1
            mapping_list.append(iter_list)
        return mapping_list

    def get_person(self, token, i: int):
        if token.upper().startswith(c.PERSON) or token.upper().startswith(c.ADDRESS):
            pair = token.upper().replace(c.PERSON, '').replace(c.ADDRESS, '').split('.')
            if self.all_unique_persons.upper() == 'TRUE':
                value = pair[1]
                mapping_value = file_utils.get_key(value, m.mapping_dictionary)
                current_file_iter = self.mapping_tokens[mapping_value]
                person_index = self.unique_person_map[current_file_iter][i]
                self.mapping_tokens[mapping_value] += 1
            else:
                key = pair[0]
                person_index = self.unique_person_map[key][i]
            return self.person_list[person_index]

    def parse_nested_tokens(self, s: str, file_num: int):
        token = file_utils.parse_string_for_token(s, self.left_token_trim, self.right_token_trim)
        if token is None:
            return s
        formatted_result = token.replace(self.left_token_trim, '').replace(self.right_token_trim, '')
        person = self.get_person(formatted_result, file_num)
        replace = data_handler.process(formatted_result, person, file_num)
        s = s.replace(token, replace, 1)
        return self.parse_nested_tokens(s, file_num)

    def duplicate_file(self, original_file_dir: str, copy_file_dir: str):
        original_file_name = file_utils.get_file_name(original_file_dir)
        original_file_path = original_file_dir + original_file_name

        with open(original_file_path, 'r') as original_file:
            for i in range(self.num_copies):
                copy_file_path = copy_file_dir + file_utils.iterate_file(original_file_name, i + 1)
                with open(copy_file_path, 'w') as copy_file:
                    line_number = 1
                    for line in original_file:
                        try:
                            parsed_line = self.parse_nested_tokens(line, i)
                        except InvalidTokenException as ite:
                            logger.error(f'{ite.token} on line {line_number} is not a recognized token. Exiting program.')
                            logger.error(ite.additional_except)
                            sys.exit()
                        copy_file.write(parsed_line)
                        line_number += 1
                    copy_file.close()
                    original_file.seek(0)
                    print(f'    {datetime.now()} - Created file {copy_file_path}')
                self.mapping_tokens = dict.fromkeys(self.mapping_tokens, 0)
            print('All files created')
            logger.info(f'Process complete! {self.num_copies} copies were created in directory: {copy_file_dir}')
            original_file.close()
