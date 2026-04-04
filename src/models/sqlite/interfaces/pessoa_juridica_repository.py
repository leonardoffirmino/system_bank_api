from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable 

class PessoaJuridicaRepositoryInterface(ABC):

    @abstractmethod
    def list_people(self) -> list[PessoaJuridicaTable]:
        pass
    
    @abstractmethod
    def create_person(self, razao_social: str, nome_fantasia:str, cnpj:str, email:str, limit_saque:float):
        pass

    @abstractmethod
    def get_person(self, client_id: int) -> PessoaJuridicaTable | None:
        pass

    @abstractmethod
    def update_saldo(self, client_id: int, saldo: float) -> PessoaJuridicaTable | None:
        pass

    @abstractmethod
    def sacar(self, client_id: int, valor: float) -> PessoaJuridicaTable | None:
        pass

    @abstractmethod
    def extrato(self, client_id: int) -> dict | None:
        pass
