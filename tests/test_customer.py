import pytest

from src.customer import Customer


@pytest.fixture
def customer_data():
    return {
        'name': 'foobar',
        'user_id': 1000,
        'longitude': 0,
        'latitude': 50
    }


@pytest.fixture
def dummy_distance():
    def _dummy_func(*args, **kwargs):
        return 100
    return _dummy_func


def test_customer_init(customer_data):
    _customer = Customer(**customer_data)
    assert _customer.name == 'foobar'
    assert _customer.user_id == 1000
    assert _customer.longitude == 0
    assert _customer.latitude == 50


def test_customer_raise(customer_data):
    with pytest.raises(NotImplementedError):
        _customer = Customer(**customer_data)
        _customer.is_near


def test_customer_no_radius_assign(customer_data):
    _customer = Customer(**customer_data)
    assert _customer.radius == 0.0


def test_customer_dummy_distance_near(
        customer_data, dummy_distance):
    Customer.get_distance = dummy_distance
    Customer.radius = 101
    _customer = Customer(**customer_data)
    assert _customer.is_near


def test_customer_dummy_distance_not_near(
        customer_data, dummy_distance):
    Customer.get_distance = dummy_distance
    Customer.radius = 99
    _customer = Customer(**customer_data)
    assert ~_customer.is_near
