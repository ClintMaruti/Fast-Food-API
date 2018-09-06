def test_get_orders(client):
    res = client.get('/api/v1/orders/')
    assert res.status_code == 200
    assert res.json

# Add the remaining test here
