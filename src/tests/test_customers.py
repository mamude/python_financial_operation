def test_customers(client):
    data = {"numero_conta": "1234", "saldo": "123.45"}
    assert client.post("/conta", json=data).status_code == 200
