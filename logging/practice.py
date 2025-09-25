import logging
import sys

def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create console handler
    console_handler = logging.Streamhandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(formatter)

    # add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


    return logger

# use logger
logger = setup_logging()
logger.info('App starter')