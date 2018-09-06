def test_home_page_appears(client):
    res = client.get('/')
    assert res.status_code == 200
    assert 'Fast-Food-Fast APi' in str(res.data)