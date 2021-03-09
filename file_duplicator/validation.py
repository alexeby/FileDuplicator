from .exception.exception import InvalidTokenException, NonUniqueMappingException
from .object.person import Person
from .common.constants import Constants as c
import logging
import re
from .common import file_utils
from .setup.mappings import Mappings as m

logger = logging.getLogger(__name__)


class Validate:
    def __init__(self, left_token_trim, right_token_trim):
        self.left_token_trim = left_token_trim
        self.right_token_trim = right_token_trim

        self.current_person = Person()
        self.unique_person_keys = set()

    # Validate mappings
    @staticmethod
    def validate_mappings():
        mappings = m.MAPPINGS
        for i in range(len(mappings)):
            mapping = mappings.pop()
            if mapping in mappings:
                logger.error(f'"{mapping}" is not a unique mapping. Mappings are not case sensitive')
                raise NonUniqueMappingException(mapping)
        logger.info('Mapping validation complete. All mappings are unique.')
        return m.MAPPINGS

    def retrieve_unique_person_keys(self, token: str):
        if token.upper().startswith(c.person) or token.upper().startswith(c.address):
            pair = token.upper().replace(c.person, '').replace(c.address, '').split('.')
            key = pair[0]
            value = pair[1]
            if value not in m.MAPPINGS:
                raise InvalidTokenException(value)
            self.unique_person_keys.add(key)

    def parse_line(self, regex_pattern: str, s: str):
        results = re.findall(regex_pattern, s)
        for result in results:
            try:
                formatted_result = result.replace(self.left_token_trim, '').replace(self.right_token_trim, '')
                self.retrieve_unique_person_keys(formatted_result)
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
