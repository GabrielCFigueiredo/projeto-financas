from platform import system

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.auth.auth import create_acess_token, SECRET_KEY, ALGORITHM, verify_token
from app.database.database import SessionLocal
from app.database.database import engine, Base
from app.models.transaction import Transaction
from app.services import FinancialSystem

Base.metadata.create_all(bind=engine)



app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API Financeira funcionando"}

@app.get("/financeira")
def list_transactions(db: Session = Depends(get_db), user=Depends(verify_token)):

    system = FinancialSystem(db)

    return system.listTransaction()

@app.post("/financeira")
def create_transaction(type: str, description: str, value: float, db: Session = Depends(get_db)):

    transaction = Transaction(
        type = type,
        value = value,
        description = description)

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return {"message": "Transação criada com sucesso"}

@app.delete("/financeira/{transaction_id}")
def delete_transaction(transaction_id: str, db: Session = Depends(get_db)):

  transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

  if not transaction:
     return {"error": "Transação não encontrada"}

  db.delete(transaction)
  db.commit()
  return {"message": "Deletado com sucesso"}


@app.get("/relatorio")
def get_report(db: Session = Depends(get_db)):
    return db.generateReport()

@app.post("/login")
def login(username: str, password: str):
    if username != "admin" and password != "123":
        return {"error": "Credenciais incorretas"}
    token = create_acess_token({"sub": username})
    return {"token": token}

