import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename='test2.log', datefmt='%d/%m/%y %H:%M:%S %p %A', level=logging.DEBUG, filemode='w')
logging.critical("This is a critical message.")
logging.debug("This is a debug message.")
logging.error("This is an error message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")