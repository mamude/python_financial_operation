from decimal import Decimal

def test_create_debit_transaction(client):
    data = {"forma_pagamento": "D", "numero_conta": "234", "valor": "10"}
    response = client.post("/transacao", json=data).json
    balance = round(Decimal(response["saldo"]), 2)
    assert balance == Decimal("170.07")
    assert response["numero_conta"] == "234"

def test_create_credit_transaction(client):
    data = {"forma_pagamento": "C", "numero_conta": "234", "valor": "10"}
    response = client.post("/transacao", json=data).json
    balance = round(Decimal(response["saldo"]), 2)
    assert balance == Decimal("169.87")
    assert response["numero_conta"] == "234"

def test_create_pix_transaction(client):
    data = {"forma_pagamento": "P", "numero_conta": "234", "valor": "10"}
    response = client.post("/transacao", json=data).json
    balance = round(Decimal(response["saldo"]), 2)
    assert balance == Decimal("170.37")
    assert response["numero_conta"] == "234"


def test_create_transaction_when_account_not_exists(client):
    data = {"forma_pagamento": "D", "numero_conta": "1234", "valor": "10"}
    assert client.post("/transacao", json=data).status_code == 401

def test_create_transaction_when_account_has_no_balance(client):
    data = {"forma_pagamento": "D", "numero_conta": "234", "valor": "1500.30"}
    assert client.post("/transacao", json=data).status_code == 401


def test_create_transaction_invalid_payment_method(client):
    data = {"forma_pagamento": "A", "numero_conta": "234", "valor": "12.32"}
    assert client.post("/transacao", json=data).status_code == 401
