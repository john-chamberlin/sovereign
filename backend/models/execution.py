from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from .base import Base

class ExecutionLog(Base):
    __tablename__ = "execution_logs"

    id = Column(Integer, primary_key=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id"), nullable=False)
    status = Column(String, default="QUEUED")
    message = Column(String)
    payload = Column(JSON)
    result = Column(JSON)
    started_at = Column(DateTime, server_default=func.now())
    finished_at = Column(DateTime)
