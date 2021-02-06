from setup.config import Config
from file_duplicator.file_handler import FileHandler


def run():
    file_handler = FileHandler(Config.API_URL)
    file_handler.duplicate_file(Config.ORIGINAL_FILE_DIR, Config.COPY_FILE_DIR, Config.NUM_COPIES, Config.REGEX_PATTERN)


if __name__ == '__main__':
    run()
