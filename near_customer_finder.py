#! /usr/local/bin/python3
import json
import logging

from src.customer import Customer


logging.basicConfig(level=logging.DEBUG)

try:
    while True:
        c_ = Customer(**json.loads(input()))

except EOFError:
    pass
