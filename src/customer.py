import logging
from collections import namedtuple


logger = logging.getLogger(__name__)


def raise_(*args, **kwargs):
    raise NotImplementedError


customer = namedtuple(
    'customer',
    ['user_id', 'longitude', 'latitude', 'name']
)


class Customer(customer):

    # these should be assigned before object usage
    get_distance = raise_
    radius = 0.0

    def __init__(self, **kwargs):
        # logger.info(self)
        pass

    @property
    def is_near(self) -> bool:
        _dist = self.get_distance(
            lon=float(self.longitude),
            lat=float(self.latitude)
        )

        if _dist <= float(self.radius):
            return True
        return False
