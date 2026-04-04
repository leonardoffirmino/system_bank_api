from sqlalchemy import Column, Integer, String, Float

from src.models.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    __limite_saque__ = 5000.00
    
    id = Column(Integer,primary_key=True, autoincrement=True)
    razao_social = Column(String(255),nullable=False)
    nome_fantasia = Column(String(255),nullable=False)
    cnpj = Column(String(18),nullable=False,unique=True)
    email = Column(String(255),nullable=False)
    limit_saque = Column(Float,nullable=False)
    saldo = Column(Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"PessoaJuridica(id={self.id}, name_company='{self.razao_social}', fantasy_name='{self.nome_fantasia}', cnpj='{self.cnpj}', email='{self.email}', limit_saque={self.limit_saque})"
    
    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor de saque deve ser maior que zero.")
        
        if valor > self.__limite_saque__:
            raise ValueError(f"O valor de saque excede o limite permitido de {self.__limite_saque__}.")
        
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")

        self.saldo -= valor
        return self.saldo
        
    def extrato(self):
        return {
            "Withdraw":{
               "id":self.id,
               "name":self.razao_social,
               "type":"PJ",
               "balance":self.saldo

            }
        }
