from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, Integer, String, Float

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(Integer,primary_key=True, autoincrement=True)
    name_company = Column(String(255),nullable=False)
    fantasy_name = Column(String(255),nullable=False)
    cnpj = Column(String(18),nullable=False,unique=True)
    email = Column(String(255),nullable=False)
    limit_withdraw = Column(Float,nullable=False)

    def __repr__(self):
        return f"PessoaJuridica(id={self.id}, name_company='{self.name_company}', fantasy_name='{self.fantasy_name}', cnpj='{self.cnpj}', email='{self.email}', limit_withdraw={self.limit_withdraw})"