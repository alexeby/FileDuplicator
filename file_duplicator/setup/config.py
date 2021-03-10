import configparser

# Init config parser
parser = configparser.ConfigParser()
parser.read('./setup/conf.ini')


class Config:
    config_section = 'Conf'
    ORIGINAL_FILE_DIR = parser.get(config_section, 'original_file_dir')
    COPY_FILE_DIR = parser.get(config_section, 'copy_file_dir')
    NUM_COPIES = int(parser.get(config_section, 'num_copies'))
    API_URL = parser.get(config_section, 'api_url')
    LEFT_TOKEN_TRIM = parser.get(config_section, 'left_token_trim')
    RIGHT_TOKEN_TRIM = parser.get(config_section, 'right_token_trim')
    CLEAR_COPY_PATH = parser.get(config_section, 'clear_copy_path')
    ALL_UNIQUE_PERSONS = parser.get(config_section, 'all_unique_persons')

    ALL_CONFIGURATIONS = [ORIGINAL_FILE_DIR, COPY_FILE_DIR, NUM_COPIES, API_URL,
                          LEFT_TOKEN_TRIM, RIGHT_TOKEN_TRIM, CLEAR_COPY_PATH, ALL_UNIQUE_PERSONS]
