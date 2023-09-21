import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_create_order_service(create_order):
    order = create_order.json
    pytest.assume(order.status.startswith('200'))
    pytest.assume(order['_id'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['date'])
    pytest.assume(order['size_id'])
    pytest.assume(order['size'])
    pytest.assume(order['detail'])