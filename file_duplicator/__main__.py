from .setup.config import Config
from file_duplicator.file_handler import FileHandler
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
        file_handler = FileHandler(Config.API_URL, Config.LEFT_TOKEN_TRIM, Config.RIGHT_TOKEN_TRIM, Config.NUM_COPIES)
        file_handler.duplicate_file(Config.ORIGINAL_FILE_DIR, Config.COPY_FILE_DIR, Config.NUM_COPIES, Config.REGEX_PATTERN)
    except Exception as ex:
        logger.exception(ex)
