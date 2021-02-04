from setup.config import Config
from file_duplicator.file_handler import duplicate_file


def run():
    duplicate_file(Config.ORIGINAL_FILE_DIR, Config.COPY_FILE_DIR, Config.NUM_COPIES, Config.REGEX_PATTERN, Config.API_URL)


if __name__ == '__main__':
    run()
