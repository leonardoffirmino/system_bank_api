from datetime import datetime

from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, DateTime, Integer, String, Float

class TransacaoTable(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, nullable=False)
    tipo_cliente = Column(String(2),nullable=False)
    tipo_transacao = Column(String(10), nullable=False)
    valor = Column(Float,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"[Transacao] - id={self.id}, client_id={self.client_id}, tipo_cliente='{self.tipo_cliente}', tipo_transacao='{self.tipo_transacao}', valor={self.valor}, created_at='{self.created_at}'"
