import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info('this is basic logging')


handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=5)

handler = TimedRotatingFileHandler('app.log', when="d", interval=1)