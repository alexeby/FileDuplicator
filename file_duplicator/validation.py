from .exception.exception import InvalidTokenException
from .object.person import Person
from .common.constants import Constants as c
import logging
import re
from .common import file_utils

logger = logging.getLogger(__name__)


class Validate:
    def __init__(self, left_token_trim, right_token_trim):
        self.left_token_trim = left_token_trim
        self.right_token_trim = right_token_trim

        self.current_person = Person()
        self.unique_person_keys = set()

    def retrieve_unique_person_keys(self, token: str):
        if token.upper().startswith(c.person) or token.upper().startswith(c.address):
            token = token.upper().replace(c.person, '').replace(c.address, '').split('.')[0]
            self.unique_person_keys.add(token)

    def parse_line(self, regex_pattern: str, s: str):
        results = re.findall(regex_pattern, s)
        for result in results:
            formatted_result = result.replace(self.left_token_trim, '').replace(self.right_token_trim, '')
            self.retrieve_unique_person_keys(formatted_result)
            try:
                replace = file_utils.get_token_value(formatted_result, self.current_person)
                s = re.sub(regex_pattern, replace, s, 1)
            except Exception as e:
                raise InvalidTokenException(result, e)
        return s

    def validate_file(self, original_file_dir: str, regex_pattern: str):
        original_file_name = file_utils.get_file_name(original_file_dir)
        original_file_path = original_file_dir + original_file_name

        with open(original_file_path, 'r') as original_file:
            line_number = 1
            logger.info('Validating file.')
            for line in original_file:
                try:
                    self.parse_line(regex_pattern, line)
                except InvalidTokenException as ite:
                    logger.error(f'{ite.token} on line {line_number} is not a recognized token. Exiting program.')
                    logger.error(ite.additional_except)
                    return False
                line_number += 1
            logger.info('File passed validation.')
            original_file.close()
            return True
