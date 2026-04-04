from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
import pytest
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository


class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
          data=[
            (
              [mock.call.query(PessoaFisicaTable)],
              [
                PessoaFisicaTable(renda_mensal=1000.0, idade=30, nome_completo="João", celular="999", categoria="A", saldo=100.0),
                PessoaFisicaTable(renda_mensal=2000.0, idade=25, nome_completo="Maria", celular="888", categoria="B", saldo=50.0)
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
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_people()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()


    assert response[0].nome_completo == "João"


def test_create_person():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    repo.create_person(1000.0, 30, "João", "999", "A", 100.0)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()


def test_list_people_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_people()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []


def test_update_saldo_error():
    mock_connection = MockConnectionNoResult()
    repo = PessoaFisicaRepository(mock_connection)

    with pytest.raises(Exception):
        repo.update_saldo(1, 200.0)

    mock_connection.session.rollback.assert_called_once()
