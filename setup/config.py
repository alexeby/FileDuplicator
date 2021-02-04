import configparser

# Init config parser
parser = configparser.ConfigParser()
parser.read('./setup/conf.ini')


class Config:
    config_section = 'Conf'
    ORIGINAL_FILE_DIR = parser.get(config_section, 'original_file_dir')
    COPY_FILE_DIR = parser.get(config_section, 'copy_file_dir')
    NUM_COPIES = int(parser.get(config_section, 'num_copies'))
    REGEX_PATTERN = parser.get(config_section, 'regex_pattern')
    API_URL = parser.get(config_section, 'api_url')
