from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable 

class PessoaJuridicaRepositoryInterface(ABC):

    @abstractmethod
    def list_people(self) -> list[PessoaJuridicaTable]:
        pass
    
    @abstractmethod
    def create_person(self, name_company: str, fantasy_name:str, cnpj:str, email:str,limit_withdraw:float):
        pass