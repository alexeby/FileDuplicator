import re
import sys
import logging
from .object.object_mapper import ObjectMapper
from .exception.exception import InvalidTokenException
from .common import file_utils
from .api_handler import get_api_data
from .common.constants import Constants as c


logger = logging.getLogger(__name__)


class FileHandler:

    def __init__(self, api_url, left_token_trim, right_token_trim, num_copies, unique_person_keys):
        self.api_url = api_url
        self.left_token_trim = left_token_trim
        self.right_token_trim = right_token_trim
        self.num_copies = num_copies
        self.unique_person_keys: set = unique_person_keys

        self.unique_person_map = self.populate_unique_person_map()

    def populate_unique_person_map(self):
        num_unique_person_keys = len(self.unique_person_keys)
        if num_unique_person_keys > 0:
            num_expected_results = num_unique_person_keys * self.num_copies
            api_results: list = get_api_data(self.api_url+str(num_expected_results))
            unique_person_map = {}
            for key in self.unique_person_keys:
                # Initialize person map
                unique_person_map[key] = []
            for key in self.unique_person_keys:
                for i in range(int(num_expected_results/num_unique_person_keys)):
                    # Populate person map with api result information
                    unique_person_map[key].append(ObjectMapper(api_results.pop()).map_person())

            return unique_person_map

    def get_person(self, token, i: int):
        if token.upper().startswith(c.person) or token.upper().startswith(c.address):
            key = token.upper().replace(c.person, '').replace(c.address, '').split('.')[0]
            return self.unique_person_map[key][i]

    def parse_line(self, regex_pattern: str, i: int, s: str):
        results = re.findall(regex_pattern, s)
        for result in results:
            formatted_result = result.replace(self.left_token_trim, '').replace(self.right_token_trim, '')
            try:
                person = self.get_person(formatted_result, i)
                replace = file_utils.get_token_value(formatted_result, person)
                s = re.sub(regex_pattern, replace, s, 1)
            except Exception as e:
                raise InvalidTokenException(result, e)
        return s

    def duplicate_file(self, original_file_dir: str, copy_file_dir: str, regex_pattern: str):
        original_file_name = file_utils.get_file_name(original_file_dir)
        original_file_path = original_file_dir + original_file_name

        with open(original_file_path, 'r') as original_file:
            for i in range(self.num_copies):
                copy_file_path = copy_file_dir + file_utils.iterate_file(original_file_name, i + 1)
                with open(copy_file_path, 'w') as copy_file:
                    line_number = 1
                    for line in original_file:
                        try:
                            parsed_line = self.parse_line(regex_pattern, i, line)
                        except InvalidTokenException as ite:
                            logger.error(f'{ite.token} on line {line_number} is not a recognized token. Exiting program.')
                            logger.error(ite.additional_except)
                            sys.exit()
                        copy_file.write(parsed_line)
                        line_number += 1
                    copy_file.close()
                    original_file.seek(0)
            logger.info(f'Process complete! {self.num_copies} copies were created in directory: {copy_file_dir}')
            original_file.close()
