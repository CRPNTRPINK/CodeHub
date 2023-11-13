from loguru import logger
import logging
import sys

# Настройка Loguru как обработчика для logging
logging.getLogger().addHandler(logging.StreamHandler())
logger.add(logging.StreamHandler(), format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

__all__ = ['logger']

