
import logging

# Create a logger object

logger = logging.getLogger(__name__)

# Set the logging level

logger.setLevel(logging.DEBUG)

# Create a file handler

handler = logging.FileHandler('app.log')

# Create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the handler

handler.setFormatter(formatter)

# Add the handler to the logger

logger.addHandler(handler)

# Log messages

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
