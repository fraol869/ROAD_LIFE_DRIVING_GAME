import logging
import os
import sys
from typing import Optional

class ScriptLogger:
    """Enhanced logging utility for MPS system"""
    
    def __init__(self, logger_name: str, log_level: int = logging.INFO):
        """Initialize logger with name and level"""
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)
        
        # Create logs directory if it doesn't exist
        self.logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Setup file handler
        log_file = os.path.join(self.logs_dir, f'{logger_name}.log')
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        
        # Setup console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        
        # Create formatters and add them to the handlers
        file_formatter = logging.Formatter(
            '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
        )
        console_formatter = logging.Formatter(
            '%(name)s-%(levelname)s-%(message)s'
        )
        
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
    def log(self, message: str, level: Optional[str] = None):
        """Send log message with specified level"""
        if level is None or level.upper() == 'INFO':
            self.logger.info(message)
        elif level.upper() == 'WARNING':
            self.logger.warning(message)
        elif level.upper() == 'ERROR':
            self.logger.error(message)
        elif level.upper() == 'DEBUG':
            self.logger.debug(message)
        elif level.upper() == 'CRITICAL':
            self.logger.critical(message)
            
    def log_error(self, error_message: str, exc_info: bool = True):
        """Log error with optional exception info"""
        self.logger.error(error_message, exc_info=exc_info)
        
    def log_warning(self, warning_message: str):
        """Log warning message"""
        self.logger.warning(warning_message)
        
    def log_info(self, info_message: str):
        """Log info message"""
        self.logger.info(info_message)
        
    def log_debug(self, debug_message: str):
        """Log debug message"""
        self.logger.debug(debug_message)
        
    def log_critical(self, critical_message: str):
        """Log critical message"""
        self.logger.critical(critical_message)
    
