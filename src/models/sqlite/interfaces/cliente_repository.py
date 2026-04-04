from typing import Protocol


class Cliente(Protocol):
    def sacar(self, value: float):
        ...

    def extrato(self):
        ...