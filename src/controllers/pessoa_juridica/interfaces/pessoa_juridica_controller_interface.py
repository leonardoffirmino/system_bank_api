from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaControllerInterface(ABC):
    @abstractmethod
    def list_people(self) -> List[PessoaJuridicaTable]:
        pass

    @abstractmethod
    def create_person(self, razao_social: str, nome_fantasia: str, cnpj: str, email: str, limit_saque: float) -> None:
        pass

    @abstractmethod
    def get_person(self, client_id: int) -> PessoaJuridicaTable | None:
        pass

    @abstractmethod
    def update_saldo(self, client_id: int, novo_saldo: float) -> PessoaJuridicaTable | None:
        pass
