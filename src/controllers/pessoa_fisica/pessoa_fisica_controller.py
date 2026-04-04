from src.controllers.pessoa_fisica.interfaces.pessoa_fisica_controller_interface import PessoaFisicaControllerInterface
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from typing import List, Any
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError


class PessoaFisicaController(PessoaFisicaControllerInterface):
    def __init__(self, repository: PessoaFisicaRepositoryInterface) -> None:
        self._repo = repository

    def list_people(self) -> dict:
        people = self.__list_people_action()
        return self.__format_response({"people": people, "count": len(people)})

    def create_person(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, categoria: str, saldo: float) -> dict:
        person = self.__create_person_action(renda_mensal, idade, nome_completo, celular, categoria, saldo)
        return self.__format_response({"person": person, "count": 1})

    def get_person(self, client_id: int) -> dict | None:
        person = self.__get_person_action(client_id)
        if person is None:
            return self.__format_response({"person": None, "count": 0})
        return self.__format_response({"person": person, "count": 1})

    def update_saldo(self, client_id: int, saldo: float) -> dict | None:
        person = self.__update_saldo_action(client_id, saldo)
        if person is None:
            return self.__format_response({"person": None, "count": 0})
        return self.__format_response({"person": person, "count": 1})

    def sacar(self, client_id: int, valor: float) -> dict | None:
        person = self.__withdraw_action(client_id, valor)
        if person is None:
            return self.__format_response({"person": None, "count": 0})
        return self.__format_response({"person": person, "count": 1})

    def extrato(self, client_id: int) -> dict | None:
        statement = self.__statement_action(client_id)
        return self.__format_response({"statement": statement, "count": 1})

    def __list_people_action(self) -> List[dict]:
        people = self._repo.list_people()
        return [
            {
                "id": p.id,
                "nome_completo": p.nome_completo,
                "idade": p.idade,
                "renda_mensal": p.renda_mensal,
                "celular": p.celular,
                "categoria": p.categoria,
                "saldo": p.saldo,
            }
            for p in people
        ]

    def __create_person_action(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, categoria: str, saldo: float) -> dict:

        if renda_mensal < 0:
            raise HttpBadRequestError("Renda mensal negativa")
        if idade <= 0:
            raise HttpBadRequestError("Idade deve ser positiva")
        if not nome_completo or not isinstance(nome_completo, str):
            raise HttpBadRequestError("Nome completo deve ser uma string não vazia")
        if saldo < 0:
            raise HttpBadRequestError("Saldo deve ser não negativo")

        self._repo.create_person(renda_mensal, idade, nome_completo, celular, categoria, saldo)
  
        people = self._repo.list_people()
        created = people[-1] if people else None
        if created is None:
            return {}
        return {
            "id": created.id,
            "nome_completo": created.nome_completo,
            "idade": created.idade,
            "renda_mensal": created.renda_mensal,
            "celular": created.celular,
            "categoria": created.categoria,
            "saldo": created.saldo,
        }

    def __get_person_action(self, client_id: int) -> dict | None:
        if client_id is None or not isinstance(client_id, int) or client_id <= 0:
            raise HttpBadRequestError("client_id deve ser um inteiro positivo")
        p = self._repo.get_person(client_id)
        if p is None:
            raise HttpNotFoundError("Pessoa não encontrada")
        return {
            "id": p.id,
            "nome_completo": p.nome_completo,
            "idade": p.idade,
            "renda_mensal": p.renda_mensal,
            "celular": p.celular,
            "categoria": p.categoria,
            "saldo": p.saldo,
        }

    def __update_saldo_action(self, client_id: int, saldo: float) -> dict | None:
        if client_id is None or not isinstance(client_id, int) or client_id <= 0:
            raise HttpBadRequestError("client_id deve ser um inteiro positivo")
        if saldo is None or not isinstance(saldo, (int, float)):
            raise HttpBadRequestError("Saldo deve ser um número")

        person = self._repo.update_saldo(client_id, saldo)
        if person is None:
            raise HttpNotFoundError("Pessoa não encontrada")
        return {
            "id": person.id,
            "nome_completo": person.nome_completo,
            "saldo": person.saldo,
        }

    def __withdraw_action(self, client_id: int, valor: float) -> dict | None:
        if client_id is None or not isinstance(client_id, int) or client_id <= 0:
            raise HttpBadRequestError("client_id deve ser um inteiro positivo")
        if valor is None or not isinstance(valor, (int, float)):
            raise HttpBadRequestError("valor deve ser um nÃºmero")

        person = self._repo.sacar(client_id, valor)
        if person is None:
            raise HttpNotFoundError("Pessoa nÃ£o encontrada")
        return {
            "id": person.id,
            "nome_completo": person.nome_completo,
            "saldo": person.saldo,
        }

    def __statement_action(self, client_id: int) -> dict:
        if client_id is None or not isinstance(client_id, int) or client_id <= 0:
            raise HttpBadRequestError("client_id deve ser um inteiro positivo")

        statement = self._repo.extrato(client_id)
        if statement is None:
            raise HttpNotFoundError("Pessoa nÃ£o encontrada")
        return statement

    def __format_response(self, person_info: dict) -> dict[str, Any]:
        return {
            "data": {
                "type": "Person",
                "count": person_info.get("count", 0),
                "attributes": person_info,
            }
        }
