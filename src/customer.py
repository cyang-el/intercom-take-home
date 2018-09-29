import logging

from src.input_consumer import customer


logger = logging.getLogger(__name__)


class Customer(customer):
    def __init__(self, **kwargs):
        logger.info(self)

    @property
    def is_close(self):
        pass
