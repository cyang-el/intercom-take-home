import logging

from src.input_consumer import customer


logger = logging.getLogger(__name__)


def raise_(*args, **kwargs):
    raise NotImplementedError


class Customer(customer):

    get_distance = raise_

    def __init__(self, **kwargs):
        logger.info(self)

    @property
    def is_near(self):
        pass
