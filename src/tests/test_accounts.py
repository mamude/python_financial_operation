def test_create_accounts(client):
    data = {"numero_conta": "1234", "saldo": "123.45"}
    assert client.post("/conta", json=data).status_code == 201


def test_create_invalid_account(client):
    data = {"numero_conta": "1234", "saldo": "invalid"}
    assert client.post("/conta", json=data).status_code == 401

def test_get_account_by_number(client):
    assert client.get("/conta?numero_conta=234").status_code == 200

def test_get_account_by_number_not_found(client):
    assert client.get("/conta?numero_conta=1234").status_code == 404