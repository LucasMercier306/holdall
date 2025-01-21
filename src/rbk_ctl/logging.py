# src/rbk_ctl/logging.py
import logging
import os

def setup_logging():
    """Configure le système de logging."""

    log_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(log_dir, exist_ok=True)

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    file_handler = logging.FileHandler(os.path.join(log_dir, 'rbk-ctl.log'))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(log_format))
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(log_format))

    logger = logging.getLogger('rbk_ctl')
    logger.setLevel(logging.DEBUG) ##level of the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger