# -*- coding: utf-8 -*-
import os
import logging
import logging.handlers

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)s] %(message)s'
DEFAULT_BACKUP_COUNT = 30
LOG_SUFFIX = "%Y%m%d"

LOG_NAME = 'sync'

from .config import LOG_PATH

class Logger(object):
    def __init__(self, log_name, log_path, log_level = logging.INFO, backup_count = DEFAULT_BACKUP_COUNT):
        self.log_name = log_name
        self.log_path = log_path
        self.log_level = log_level
        self.backup_count = backup_count

        self.log_handler = logging.handlers.WatchedFileHandler(self.log_path)
        self.log_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        self.logger = logging.getLogger(self.log_name) 
        self.logger.addHandler(self.log_handler)
        self.logger.setLevel(log_level)  

        self.level_dict = {
                'debug' : logging.DEBUG,
                'info' : logging.INFO,
                'warning' : logging.WARNING,
                'error' : logging.ERROR,
                'critical' : logging.CRITICAL
                }

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
    def set_level(self, log_level):
         level = None
         if log_level in self.level_dict:
             level = self.level_dict[log_level]
         else:
             self.warning('%s is invalid, will use default log level INFO' % (log_level))
             level = logging.INFO
 
         self.logger.setLevel(level)
 
def get_logger_by_name(log_name = LOG_NAME):
    return logging.getLogger(log_name)
 
def init_logger(log_path, log_name = LOG_NAME, log_level = 'info'):
    logger = Logger(log_name, os.path.join(log_path, u'{0}.log'.format(log_name)))
    logger.set_level(log_level)
    return logger


init_logger(LOG_PATH)
APP_LOG = get_logger_by_name()
