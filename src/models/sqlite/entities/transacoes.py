from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, DateTime, Integer, String, Float

class TransacaoTable(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, nullable=False)
    type_client = Column(String(2),nullable=False)
    type_transaction = Column(String(10), nullable=False)
    value = Column(Float,nullable=False)
    created_at = Column(DateTime, default=DateTime.utcnow)

    def __repr__(self):
        return f"[Transacao] - id={self.id}, client_id={self.client_id}, type_client='{self.type_client}', type_transaction='{self.type_transaction}', value={self.value}, created_at='{self.created_at}'"