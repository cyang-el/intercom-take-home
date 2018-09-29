#! /usr/local/bin/python3
import json
import os
import logging

from src.customer import Customer


if __name__ == '__main__':
    lon = os.environ['intercom_lon']
    lat = os.environ['intercom_lat']
    radius = os.environ['radius']

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    try:
        while True:
            c_ = Customer(**json.loads(input()))

    except EOFError:
        logger.info('EOF, Finished.')
