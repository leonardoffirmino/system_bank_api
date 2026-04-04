import pytest
from src.controllers.pessoa_juridica.pessoa_juridica_controller import PessoaJuridicaController
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError


class MockCompany:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, email, limit_saque, saldo=None):
        self.id = id
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.email = email
        self.limit_saque = limit_saque
        self.saldo = saldo


class MockRepo:
    def __init__(self):
        self._items = []

    def list_people(self):
        return self._items

    def create_person(self, razao_social, nome_fantasia, cnpj, email, limit_saque):
        new_id = len(self._items) + 1
        c = MockCompany(new_id, razao_social, nome_fantasia, cnpj, email, limit_saque, saldo=0)
        self._items.append(c)

    def get_person(self, client_id):
        for c in self._items:
            if c.id == client_id:
                return c
        return None

    def update_saldo(self, client_id, novo_saldo):
        c = self.get_person(client_id)
        if not c:
            return None
        c.saldo = novo_saldo
        return c

    def sacar(self, client_id, valor):
        c = self.get_person(client_id)
        if not c:
            return None
        if valor > c.saldo:
            raise ValueError("Saldo insuficiente")
        c.saldo -= valor
        return c

    def extrato(self, client_id):
        c = self.get_person(client_id)
        if not c:
            return None
        return {
            "account": {"Withdraw": {"id": c.id, "name": c.razao_social, "type": "PJ", "balance": c.saldo}},
            "transactions": [],
        }


def test_create_and_list_format():
    repo = MockRepo()
    controller = PessoaJuridicaController(repo)
    controller.create_person("Razao Ltda", "Razao", "12.345.678/0001-90", "a@b.com", 1000.0)
    res = controller.list_people()

    assert res["data"]["type"] == "Person"
    assert res["data"]["count"] == 1
    assert res["data"]["attributes"]["people"][0]["razao_social"] == "Razao Ltda"


def test_create_person_validation_error():
    repo = MockRepo()
    controller = PessoaJuridicaController(repo)

    with pytest.raises(HttpBadRequestError):
        controller.create_person("", "X", "", "e@e.com", -1)


def test_get_and_update_errors():
    repo = MockRepo()
    controller = PessoaJuridicaController(repo)

    with pytest.raises(HttpNotFoundError):
        controller.get_person(1)


    controller.create_person("Razao Ltda", "Razao", "12.345.678/0001-90", "a@b.com", 1000.0)
    res = controller.update_saldo(1, 2500.0)
    assert res["data"]["attributes"]["person"]["saldo"] == 2500.0


def test_sacar_and_extrato():
    repo = MockRepo()
    controller = PessoaJuridicaController(repo)
    controller.create_person("Razao Ltda", "Razao", "12.345.678/0001-90", "a@b.com", 1000.0)
    controller.update_saldo(1, 2500.0)

    withdraw_response = controller.sacar(1, 500.0)
    assert withdraw_response["data"]["attributes"]["person"]["saldo"] == 2000.0

    statement_response = controller.extrato(1)
    assert statement_response["data"]["attributes"]["statement"]["account"]["Withdraw"]["balance"] == 2000.0
