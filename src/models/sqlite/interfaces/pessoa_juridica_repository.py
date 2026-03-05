from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable 

class PessoaJuridicaRepositoryInterface(ABC):

    @abstractmethod
    def list_people(self) -> list[PessoaJuridicaTable]:
        pass
    
    @abstractmethod
    def create_person(self, razao_social: str, nome_fantasia:str, cnpj:str, email:str, limit_saque:float):
        pass