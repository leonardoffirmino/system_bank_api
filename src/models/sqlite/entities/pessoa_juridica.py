from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, Integer, String, Float

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(Integer,primary_key=True, autoincrement=True)
    razao_social = Column(String(255),nullable=False)
    nome_fantasia = Column(String(255),nullable=False)
    cnpj = Column(String(18),nullable=False,unique=True)
    email = Column(String(255),nullable=False)
    limit_saque = Column(Float,nullable=False)

    def __repr__(self):
        return f"PessoaJuridica(id={self.id}, name_company='{self.razao_social}', fantasy_name='{self.nome_fantasia}', cnpj='{self.cnpj}', email='{self.email}', limit_saque={self.limit_saque})"