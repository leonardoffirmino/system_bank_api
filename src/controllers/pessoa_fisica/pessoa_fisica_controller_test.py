import pytest
from src.controllers.pessoa_fisica.pessoa_fisica_controller import PessoaFisicaController
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError


class MockPerson:
    def __init__(self, id, nome_completo, idade, renda_mensal, celular, categoria, saldo):
        self.id = id
        self.nome_completo = nome_completo
        self.idade = idade
        self.renda_mensal = renda_mensal
        self.celular = celular
        self.categoria = categoria
        self.saldo = saldo


class MockRepo:
    def __init__(self):
        self._people = []

    def list_people(self):
        return self._people

    def create_person(self, renda_mensal, idade, nome_completo, celular, categoria, saldo):
        new_id = len(self._people) + 1
        p = MockPerson(new_id, nome_completo, idade, renda_mensal, celular, categoria, saldo)
        self._people.append(p)

    def get_person(self, client_id):
        for p in self._people:
            if p.id == client_id:
                return p
        return None

    def update_saldo(self, client_id, saldo):
        p = self.get_person(client_id)
        if not p:
            return None
        p.saldo = saldo
        return p

    def sacar(self, client_id, valor):
        p = self.get_person(client_id)
        if not p:
            return None
        if valor > p.saldo:
            raise ValueError("Saldo insuficiente")
        p.saldo -= valor
        return p

    def extrato(self, client_id):
        p = self.get_person(client_id)
        if not p:
            return None
        return {
            "account": {"Withdraw": {"id": p.id, "name": p.nome_completo, "type": "PF", "balance": p.saldo}},
            "transactions": [],
        }


def test_list_people_format():
    repo = MockRepo()
    repo.create_person(1000, 30, "João", "999", "A", 100)
    controller = PessoaFisicaController(repo)
    response = controller.list_people()

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["people"][0]["nome_completo"] == "João"


def test_create_person_validation_error():
    repo = MockRepo()
    controller = PessoaFisicaController(repo)

    with pytest.raises(HttpBadRequestError):
        controller.create_person(-1, 30, "Invalid", "999", "A", 100)


def test_get_person_not_found():
    repo = MockRepo()
    controller = PessoaFisicaController(repo)

    with pytest.raises(HttpNotFoundError):
        controller.get_person(1)


def test_update_saldo_success_and_not_found():
    repo = MockRepo()
    repo.create_person(1000, 30, "João", "999", "A", 100)
    controller = PessoaFisicaController(repo)

    res = controller.update_saldo(1, 500)
    assert res["data"]["attributes"]["person"]["saldo"] == 500

    with pytest.raises(HttpNotFoundError):
        controller.update_saldo(99, 100)


def test_sacar_and_extrato():
    repo = MockRepo()
    repo.create_person(1000, 30, "JoÃ£o", "999", "A", 100)
    controller = PessoaFisicaController(repo)

    withdraw_response = controller.sacar(1, 40)
    assert withdraw_response["data"]["attributes"]["person"]["saldo"] == 60

    statement_response = controller.extrato(1)
    assert statement_response["data"]["attributes"]["statement"]["account"]["Withdraw"]["balance"] == 60
