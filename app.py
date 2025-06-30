from books_recommender.exception.exception_handler import AppException
import sys
from books_recommender.logger import logger
try: 
    a=3/0
except Exception as e:

    logger.info(e)
    raise AppException(e,sys) from e