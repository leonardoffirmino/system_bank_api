from sqlalchemy import Column, Integer, String, Float
from src.models.sqlite.settings.base import Base

class PessoaFisicaTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(Integer,primary_key=True, autoincrement=True)
    renda_mensal = Column(Float,nullable=False)
    idade = Column(Integer,nullable=False)
    nome_completo = Column(String(255),nullable=False)
    celular = Column(String(25),nullable=False)
    categoria = Column(String(100),nullable=False)
    saldo = Column(Float,nullable=False)

    def __repr__(self):
        return f"PessoaFisica(id={self.id},name='{self.nome_completo}', age={self.idade}, renda_mensal={self.renda_mensal}, phone='{self.celular}', category='{self.categoria}', balance={self.saldo})"