import logging

from .consts import LOG_FILE

logging.basicConfig(level=logging.DEBUG, filename=LOG_FILE, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
