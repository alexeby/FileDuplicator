from .setup.config import Config
from file_duplicator.file_handler import FileHandler
from file_duplicator.validation import Validate
import logging.config

try:
    logging.config.fileConfig(fname='setup/log.ini', disable_existing_loggers=False)
except:
    print('Log directory does not exist. Logging has been disabled.')

logger = logging.getLogger(__name__)


def main():
    # Log all configuration settings
    logger.info(Config.ALL_CONFIGURATIONS)

    try:
        file_validator = Validate(Config.LEFT_TOKEN_TRIM, Config.RIGHT_TOKEN_TRIM)
        is_valid = file_validator.validate_file(Config.ORIGINAL_FILE_DIR, Config.REGEX_PATTERN)
        unique_person_keys = file_validator.unique_person_keys

        if is_valid:
            file_handler = FileHandler(Config.API_URL, Config.LEFT_TOKEN_TRIM, Config.RIGHT_TOKEN_TRIM,
                                       Config.NUM_COPIES, unique_person_keys)
            file_handler.duplicate_file(Config.ORIGINAL_FILE_DIR, Config.COPY_FILE_DIR, Config.REGEX_PATTERN)
        else:
            logger.error('Exiting program because file is invalid.')
    except Exception as ex:
        logger.exception(ex)
