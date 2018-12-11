import logging
import time
from logging import handlers

time_flag = time.time()
LOG_FILENAME = 'E:\yuntu_App\log\\run.log'


# Color escape string
COLOR_RED = '\033[1;31m'
COLOR_GREEN = '\033[1;32m'
COLOR_YELLOW = '\033[1;33m'
COLOR_BLUE = '\033[1;34m'
COLOR_PURPLE = '\033[1;35m'
COLOR_CYAN = '\033[1;36m'
COLOR_GRAY = '\033[1;37m'
COLOR_WHITE = '\033[1;38m'
COLOR_RESET = '\033[1;0m'

# Define log color
LOG_COLORS = {
    'DEBUG': COLOR_BLUE + '%s' + COLOR_RESET,
    'INFO': COLOR_GREEN + '%s' + COLOR_RESET,
    'WARNING': COLOR_YELLOW + '%s' + COLOR_RESET,
    'ERROR': COLOR_RED + '%s' + COLOR_RESET,
    'CRITICAL': COLOR_RED + '%s' + COLOR_RESET,
    'EXCEPTION': COLOR_RED + '%s' + COLOR_RESET,
}

class log_colour(logging.Formatter):

    def __init__(self, fmt=None, datefmt=None):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        level_name = record.levelname
        msg = logging.Formatter.format(self, record)
        return LOG_COLORS.get(level_name, '%s') % msg


def get_logger():
    logger = logging.Logger('Automation')
    logger.setLevel(0)
    terminal = logging.StreamHandler()
    terminal.setLevel(logging.DEBUG)

    log_file = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=10 * 1024 * 1024, backupCount=3)
    log_file.setLevel(logging.INFO)

    formatter_ter = log_colour(
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    formatter_log = logging.Formatter(
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

    terminal.setFormatter(formatter_ter)
    log_file.setFormatter(formatter_log)

    logger.addHandler(terminal)
    logger.addHandler(log_file)

    return logger

def set_log_file(logfilename):
    global LOG_FILENAME
    LOG_FILENAME = logfilename
