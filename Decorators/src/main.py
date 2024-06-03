import logging
from functools import wraps

def logger(func):
    logging.basicConfig(filename = f'{__file__[:-2]}log',
                        filemode = 'w',
                        format = '[%(levelname)s] (%(asctime)s): %(message)s (Line: %(lineno)s [%(filename)s])',
                        datefmt = '%Y-%m-%d %H:%M:%S',
                        encoding = 'utf-8',
                        level = logging.DEBUG)
    logging.info(func)

@logger
def tester():
    print(__name__)

if __name__ == "__main__":
    tester()