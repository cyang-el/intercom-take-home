import os
import json
import logging
from typing import Generator


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def read_input_file() -> Generator[str, None, None]:
    with open(os.environ['input_file'], 'r') as file_:
        line = file_.readline()
        while line:
            yield line
            line = file_.readline()


def output_queue(queue):
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
