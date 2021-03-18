from .setup.config import Config
from file_duplicator.file_handler import FileHandler
from file_duplicator.validation import Validate
import logging.config
import os
import glob

try:
    logging.config.fileConfig(fname='setup/log.ini', disable_existing_loggers=False)
except:
    print('Log directory does not exist. Logging has been disabled.')

logger = logging.getLogger(__name__)


def main():
    # Log all configuration settings
    logger.info(Config.ALL_CONFIGURATIONS)

    try:

        file_validator = Validate(Config.LEFT_TOKEN_TRIM, Config.RIGHT_TOKEN_TRIM, Config.ALL_UNIQUE_PERSONS)
        is_valid = file_validator.validate_file(Config.ORIGINAL_FILE_DIR)
        unique_person_keys = file_validator.unique_person_keys
        num_records_per_file = file_validator.num_records_per_file
        mapping_tokens = file_validator.mapping_tokens
        file_validator.validate_mappings()

        # Clear out directory
        if Config.CLEAR_COPY_PATH.upper() == 'TRUE':
            files = glob.glob(Config.COPY_FILE_DIR+'*')
            for f in files:
                os.remove(f)

        if is_valid:
            file_handler = FileHandler(Config.API_URL, Config.LEFT_TOKEN_TRIM, Config.RIGHT_TOKEN_TRIM,
                                       Config.NUM_COPIES, unique_person_keys, Config.ALL_UNIQUE_PERSONS,
                                       num_records_per_file, mapping_tokens)
            file_handler.duplicate_file(Config.ORIGINAL_FILE_DIR, Config.COPY_FILE_DIR)
        else:
            logger.error('Exiting program because file is invalid.')
    except Exception as ex:
        logger.exception(ex)
