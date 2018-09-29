import json
import os
import logging
from functools import partial
from typing import Generator

from src.customer import Customer
from src.distance import get_distance
from src.output_handler import CustomerQueue


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def setup_distance_method():
    _get_distance = partial(
        get_distance,
        pin_lon=float(os.environ['intercom_lon']),
        pin_lat=float(os.environ['intercom_lat']))
    Customer.get_distance = _get_distance
    Customer.radius = float(os.environ['radius'])


def read_input_file() -> Generator[str, None, None]:
    with open(os.environ['input_file'], 'r') as file_:
        line = file_.readline()
        while line:
            yield line
            line = file_.readline()


def output_near_customers(queue):
    output_filename = os.environ['output_file']
    with open(output_filename, 'w') as file_:
        while True:
            try:
                file_.write('{}\n'.format(
                    json.dumps(queue.pop())))
            except IndexError:
                logger.info(
                    f'Done. Check {output_filename} '
                    'for output.')
                break


if __name__ == '__main__':
    setup_distance_method()
    queue = CustomerQueue()
    for ln in read_input_file():
        customer = Customer(**json.loads(ln))
        if customer.is_near:
            queue.push(
                name=customer.name,
                user_id=customer.user_id)
    output_near_customers(queue)
