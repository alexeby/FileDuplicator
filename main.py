from setup.config import Config
from file_duplicator.file_handler import FileHandler
import logging.config
import sys

logging.config.fileConfig(fname='setup/log.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def run():
    # Log all configuration settings
    logger.info(Config.ALL_CONFIGURATIONS)

    file_handler = FileHandler(Config.API_URL, Config.LEFT_TOKEN_TRIM, Config.RIGHT_TOKEN_TRIM)
    file_handler.duplicate_file(Config.ORIGINAL_FILE_DIR, Config.COPY_FILE_DIR, Config.NUM_COPIES, Config.REGEX_PATTERN)


if __name__ == '__main__':
    try:
        run()
    except:
        e = sys.exc_info()[0]
        logger.exception(e)
