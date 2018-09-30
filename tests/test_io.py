from contextlib import contextmanager
import tempfile
import os
import json

from src.io import (
    read_input_file,
    output_queue
)


@contextmanager
def mock_env_input_file():
    _input_file = os.environ['input_file']
    try:
        os.environ['input_file'] = 'tests/data/input.txt'
        yield None
    finally:
        os.environ['input_file'] = _input_file


def test_read_input_file():
    expected = [
        {"latitude": "52.986375",
         "user_id": 12,
         "name": "Christina McArdle",
         "longitude": "-6.043701"},
        {"latitude": "51.92893",
         "user_id": 1,
         "name": "Alice Cahill",
         "longitude": "-10.27699"},
        {"latitude": "51.8856167",
         "user_id": 2,
         "name": "Ian McArdle",
         "longitude": "-10.4240951"},
        {"latitude": "52.3191841",
         "user_id": 3, "name": "Jack Enright",
         "longitude": "-8.5072391"},
        {"latitude": "53.807778",
         "user_id": 28,
         "name": "Charlie Halligan",
         "longitude": "-7.714444"}
    ]
    with mock_env_input_file():
        for ln, exp_ln in zip(read_input_file(), expected):
            assert json.loads(ln) == exp_ln


@contextmanager
def mock_env_output_file():
    fp = tempfile.NamedTemporaryFile()
    _output_file = os.environ['output_file']
    try:
        os.environ['output_file'] = fp.name
        yield fp.name
    finally:
        os.environ['output_file'] = _output_file


def test_output_queue():
    data = {'1': '1'}, {'2': '2'}, {'3': '3'}
    queue = list(data)[::-1]  # or reverse()
    with mock_env_output_file() as fname:
        output_queue(queue)
        with open(fname, 'r') as fp:
            for ln in data:
                assert ln == json.loads(fp.readline())
            assert not fp.readline()  # EOF
