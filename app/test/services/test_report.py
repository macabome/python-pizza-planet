import pytest

def test_create_order_service(create_order):
    order = create_order.json
    pytest.assume(create_order.status.startswith('200'))
    pytest.assume(order['_id'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_phone'])

def test_get_report(app, create_orders):
    client = app.test_client()
    
    # Realizar una solicitud GET a la ruta /report
    response = client.get('/report/')
    
    # Verificar que el código de respuesta sea 200 (éxito)
    assert response.status_code == 200
    
