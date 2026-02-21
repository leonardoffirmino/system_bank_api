from abc import ABC, abstractmethod


class ClienteRepositoryInterface(ABC):

    @abstractmethod
    def sacar(self, value: float):
        pass
    
    @abstractmethod
    def extrato(self):
        pass