import logging

logging.basicConfig(filename='test.log', level = logging.DEBUG)
logging.critical("This is a critical message.")
logging.debug("This is a debug message.")
logging.error("This is an error message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")