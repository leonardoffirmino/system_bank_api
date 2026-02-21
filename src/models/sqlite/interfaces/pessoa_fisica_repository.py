from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaRepositoryInterface(ABC):

    @abstractmethod
    def create_person(self, renda_mensal: float,age: int, name:str, phone:str,category:str, balance:float):
        pass
    
    @abstractmethod
    def list_people(self) -> list[PessoaFisicaTable]:
        pass