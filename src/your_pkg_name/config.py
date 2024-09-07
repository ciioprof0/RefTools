#!/usr/bin/env python
# -*- coding: utf-8 -*-
#src/your_pkg_name/config.py

"""This module contains the configuration variables for the application."""

import os
import logging

class Config:
    """
    Base configuration class for the application.
    """
    LOG_FILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs/dev')

    if not os.path.exists(LOG_FILE_DIR):
        os.makedirs(LOG_FILE_DIR)  # Ensure the logs directory exists

    LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, 'application.log')
    ERROR_LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, 'error.log')

    LOG_LEVEL = logging.INFO  # Default log level
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    @staticmethod
    def init_logging() -> logging.Logger:
        """
        Sets up the logging configuration for the application.

        Returns:
            A configured logger instance.
        """
        logging.basicConfig(
            level=Config.LOG_LEVEL,
            format=Config.LOG_FORMAT,
            handlers=[
                logging.FileHandler(Config.LOG_FILE_PATH),  # Main log file
                logging.FileHandler(Config.ERROR_LOG_FILE_PATH),  # Error log file
                logging.StreamHandler()  # Log to console
            ]
        )
        logger = logging.getLogger(__name__)
        return logger
