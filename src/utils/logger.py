import logging
from typing import Optional


def setup_logger(name: Optional[str] = None) -> logging.Logger:
    """Configurar y retornar un logger."""
    logger = logging.getLogger(name or __name__)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger