from os import path
import time
import logging
import logging.config
import kflogs

# Get current working directory
filePath = path.dirname(path.abspath(__file__))

# Get the full path to the logging.conf file
logConfigFile = path.join(filePath, 'test_config.conf')

# Load the config file
logging.config.fileConfig(logConfigFile)

# Set timestamps to UTC for compatibility with 3rd party services
logging.Formatter.converter = time.gmtime

# Main logger
logger = logging.getLogger('root')
logger.debug('Debug...')
logger.info('Info')
logger.warning('Warning!')
logger.critical('Critical!!')