from src.controllers.pessoa_juridica.interfaces.pessoa_juridica_controller_interface import PessoaJuridicaControllerInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from typing import List, Any


class PessoaJuridicaController(PessoaJuridicaControllerInterface):
    def __init__(self, repository: PessoaJuridicaRepositoryInterface) -> None:
        self._repo = repository

    def list_people(self) -> dict:
        people = self.__list_people_action()
        return self.__format_response({"people": people, "count": len(people)})

    def create_person(self, razao_social: str, nome_fantasia: str, cnpj: str, email: str, limit_saque: float) -> dict:
        person = self.__create_person_action(razao_social, nome_fantasia, cnpj, email, limit_saque)
        return self.__format_response({"person": person, "count": 1})

    def get_person(self, client_id: int) -> dict | None:
        person = self.__get_person_action(client_id)
        if person is None:
            return self.__format_response({"person": None, "count": 0})
        return self.__format_response({"person": person, "count": 1})

    def update_saldo(self, client_id: int, novo_saldo: float) -> dict | None:
        person = self.__update_saldo_action(client_id, novo_saldo)
        if person is None:
            return self.__format_response({"person": None, "count": 0})
        return self.__format_response({"person": person, "count": 1})

    
    def __list_people_action(self) -> List[dict]:
        people = self._repo.list_people()
        return [
            {
                "id": p.id,
                "razao_social": p.razao_social,
                "nome_fantasia": p.nome_fantasia,
                "cnpj": p.cnpj,
                "email": p.email,
                "limit_saque": p.limit_saque,
                "saldo": getattr(p, "saldo", None),
            }
            for p in people
        ]

    def __create_person_action(self, razao_social: str, nome_fantasia: str, cnpj: str, email: str, limit_saque: float) -> dict:
        if not razao_social or not isinstance(razao_social, str):
            raise ValueError("Razao social deve ser uma string não vazia")
        if not cnpj or not isinstance(cnpj, str):
            raise ValueError("CNPJ não localizado: cnpj deve ser uma string não vazia")
        if limit_saque is None or limit_saque < 0:
            raise ValueError("Limite de saque deve ser um número positivo")

        self._repo.create_person(razao_social, nome_fantasia, cnpj, email, limit_saque)
        people = self._repo.list_people()
        created = people[-1] if people else None
        if created is None:
            return {}
        return {
            "id": created.id,
            "razao_social": created.razao_social,
            "nome_fantasia": created.nome_fantasia,
            "cnpj": created.cnpj,
            "email": created.email,
            "limit_saque": created.limit_saque,
            "saldo": getattr(created, "saldo", None),
        }

    def __get_person_action(self, client_id: int) -> dict | None:
        if client_id is None or not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Não localizado: client_id deve ser um inteiro positivo")
        p = self._repo.get_person(client_id)
        if p is None:
            return None
        return {
            "id": p.id,
            "razao_social": p.razao_social,
            "nome_fantasia": p.nome_fantasia,
            "cnpj": p.cnpj,
            "email": p.email,
            "limit_saque": p.limit_saque,
            "saldo": getattr(p, "saldo", None),
        }

    def __update_saldo_action(self, client_id: int, novo_saldo: float) -> dict | None:
        if client_id is None or not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Não localizado: client_id deve ser um inteiro positivo")
        if novo_saldo is None or not isinstance(novo_saldo, (int, float)):
            raise ValueError("Novo saldo deve ser um número")

        person = self._repo.update_saldo(client_id, novo_saldo)
        if person is None:
            return None
        return {
            "id": person.id,
            "razao_social": person.razao_social,
            "saldo": getattr(person, "saldo", None),
        }

    def __format_response(self, person_info: dict) -> dict[str, Any]:
        return {
            "data": {
                "type": "Person",
                "count": person_info.get("count", 0),
                "attributes": person_info,
            }
        }
