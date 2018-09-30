import pytest

from src.output_handler import CustomerQueue


to_sortby_user_id = [
    {'user_id': id_, 'name': 'foo'}
    for id_ in (100, 2, 5, -1)
]


to_sortby_user_id_expected = [
    {'user_id': str(id_), 'name': 'foo'}
    for id_ in (-1, 2, 5, 100)
]


to_sortby_name = [
    {'user_id': 1, 'name': name}
    for name in ('Dan', 'Carol', 'Ben', 'Alice')
]


to_sortby_name_expected = [
    {'user_id': '1', 'name': name}
    for name in ('Alice', 'Ben', 'Carol', 'Dan')
]


@pytest.mark.parametrize(
    'to_push, expected',
    [(to_sortby_user_id, to_sortby_user_id_expected),
     (to_sortby_name, to_sortby_name_expected)])
def test_customer_queue(to_push, expected):
    queue = CustomerQueue()
    for customer in to_push:
        queue.push(**customer)

    for customer_expected in expected:
        assert queue.pop() == customer_expected

    with pytest.raises(IndexError):
        queue.pop()
