from sqlalchemy import Column,String,Float
from app.database.database import Base
import  uuid

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    type = Column(String)
    value = Column(Float)
    description = Column(String)