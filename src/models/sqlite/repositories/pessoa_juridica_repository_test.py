from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
import pytest
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository


class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
          data=[
            (
              [mock.call.query(PessoaJuridicaTable)],
              [
                PessoaJuridicaTable(razao_social="Razao Ltda", nome_fantasia="Razao", cnpj="12.345.678/0001-90", email="a@b.com", limit_saque=1000.0, saldo=500.0),
                PessoaJuridicaTable(razao_social="Comp SA", nome_fantasia="Comp", cnpj="98.765.432/0001-10", email="x@y.com", limit_saque=2000.0, saldo=150.0)
              ]
            )
          ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass
    def __call__(self):
        return self


class MockConnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass
    def __call__(self):
        return self


def test_list_people():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    response = repo.list_people()

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].razao_social == "Razao Ltda"


def test_create_person():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    repo.create_person("Razao Ltda", "Razao", "12.345.678/0001-90", "a@b.com", 1000.0)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()


def test_list_people_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaJuridicaRepository(mock_connection)
    response = repo.list_people()

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []


def test_update_saldo_success():
   
    session = mock.Mock()
    person = PessoaJuridicaTable(razao_social="X", nome_fantasia="X", cnpj="11.11", email="e@e.com", limit_saque=1000.0, saldo=100.0)
    session.query.return_value.filter.return_value.first.return_value = person
    conn = mock.MagicMock()
    conn.__enter__.return_value = conn
    conn.session = session

    repo = PessoaJuridicaRepository(lambda: conn)
    updated = repo.update_saldo(person.id, 150.0)

    session.commit.assert_called_once()
    assert updated.saldo == 150.0


def test_update_saldo_error():
    mock_connection = MockConnectionNoResult()
    repo = PessoaJuridicaRepository(mock_connection)

    with pytest.raises(Exception):
        repo.update_saldo(1, 200.0)

    mock_connection.session.rollback.assert_called_once()
