from src.controllers.pessoa_fisica.interfaces.pessoa_fisica_controller_interface import PessoaFisicaControllerInterface
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from typing import List, Any


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
            raise ValueError("Renda mensal negativa")
        if idade <= 0:
            raise ValueError("Idade deve ser positiva")
        if not nome_completo or not isinstance(nome_completo, str):
            raise ValueError("Nome completo deve ser uma string não vazia")
        if saldo < 0:
            raise ValueError("Saldo deve ser não negativo")

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
            raise ValueError("Não localizado: client_id deve ser um inteiro positivo")
        p = self._repo.get_person(client_id)
        if p is None:
            return None
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
            raise ValueError("Não localizado: client_id deve ser um inteiro positivo")
        if saldo is None or not isinstance(saldo, (int, float)):
            raise ValueError("Saldo deve ser um número")

        person = self._repo.update_saldo(client_id, saldo)
        if person is None:
            return None
        return {
            "id": person.id,
            "nome_completo": person.nome_completo,
            "saldo": person.saldo,
        }

    def __format_response(self, person_info: dict) -> dict[str, Any]:
        return {
            "data": {
                "type": "Person",
                "count": person_info.get("count", 0),
                "attributes": person_info,
            }
        }
