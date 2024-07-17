def test_create_customers(client):
    data = {"numero_conta": "1234", "saldo": "123.45"}
    assert client.post("/conta", json=data).status_code == 200


def test_create_invalid_customer(client):
    data = {"numero_conta": "1234", "saldo": "invalid"}
    assert client.post("/conta", json=data).status_code == 401
