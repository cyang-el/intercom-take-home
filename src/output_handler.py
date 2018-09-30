import heapq
from typing import Dict


class CustomerQueue:
    def __init__(self):
        self._queue = []

    def push(self, *, name: str, user_id: int):
        heapq.heappush(self._queue, (user_id, name))

    def pop(self) -> Dict[str, str]:
        customer = heapq.heappop(self._queue)
        return {
            'user_id': str(customer[0]),
            'name': customer[1]
        }
