def test_create_transaction(client):
    data = {"forma_pagamento": "D", "numero_conta": "1234", "valor": "12.32"}
    assert client.post("/transacao", json=data).status_code == 201

def test_create_transaction_invalid_payment_method(client):
    data = {"forma_pagamento": "A", "numero_conta": "1234", "valor": "12.32"}
    assert client.post("/transacao", json=data).status_code == 401
