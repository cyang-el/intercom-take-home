import os
import json
import logging
from functools import partial

from src.customer import Customer
from src.distance import get_distance
from src.output_handler import CustomerQueue
from src.io import (
    read_input_file,
    output_queue
)


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def setup_distance_method():
    _get_distance = partial(
        get_distance,
        pin_lon=float(os.environ['intercom_lon']),
        pin_lat=float(os.environ['intercom_lat']))
    Customer.get_distance = _get_distance
    Customer.radius = float(os.environ['radius'])


def main():
    queue = CustomerQueue()
    for ln in read_input_file():
        try:
            customer = Customer(**json.loads(ln))
        except TypeError:
            logger.warn(
                f'Encounter Non compatible data format: {ln}')
            continue
        if customer.is_near:
            queue.push(
                name=customer.name,
                user_id=customer.user_id)
    output_queue(queue)


if __name__ == '__main__':
    setup_distance_method()
    main()
