import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # handlers inherit ?

# handlers creation
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logs.log')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.ERROR)

# formatters
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# add handlers to logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
