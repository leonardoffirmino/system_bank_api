from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaControllerInterface(ABC):
    @abstractmethod
    def list_people(self) -> List[PessoaFisicaTable]:
        pass

    @abstractmethod
    def create_person(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, categoria: str, saldo: float) -> None:
        pass

    @abstractmethod
    def get_person(self, client_id: int) -> PessoaFisicaTable | None:
        pass

    @abstractmethod
    def update_saldo(self, client_id: int, saldo: float) -> PessoaFisicaTable | None:
        pass

    @abstractmethod
    def sacar(self, client_id: int, valor: float) -> PessoaFisicaTable | None:
        pass

    @abstractmethod
    def extrato(self, client_id: int) -> dict | None:
        pass
