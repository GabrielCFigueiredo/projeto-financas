from app.database.database import engine, Base
from app.models.transaction import Transaction

print("Criando tabelas...")

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")