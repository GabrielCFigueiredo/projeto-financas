from app.database.database import engine
from app.models.transaction import Transaction
from app.database.database import Base

Base.metadata.create_all(bind=engine)

print("Banco criado com sucesso")