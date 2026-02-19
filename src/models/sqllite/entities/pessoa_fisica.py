from sqlalchemy import Column, Integer, String, REAL
from src.models.sqllite.settings.base import Base

class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(Integer,primary_key=True, autoincrement=True)
    renda_mensal = Column(REAL,nullable=False)
    age = Column(Integer,nullable=False)
    name = Column(String(255),nullable=False)
    phone = Column(String(25),nullable=False)
    category = Column(String(100),nullable=False)
    balance = Column(REAL,nullable=False)

    def __repr__(self):
        return f"PessoaFisica(id={self.id},name='{self.name}', age={self.age}, renda_mensal={self.renda_mensal}, phone='{self.phone}', category='{self.category}', balance={self.balance})"