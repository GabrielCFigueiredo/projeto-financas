from fastapi import FastAPI
from app.database.database import SessionLocal
from app.models.transaction import Transaction

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Financeira funcionando"}

@app.get("/financeira")
def list_transactions():

    db = SessionLocal()

    transactions = db.query(Transaction).all()

    return transactions

@app.post("/financeira")
def create_transaction(type: str, description: str, value: float):
    db = SessionLocal()
    transaction = Transaction(
        type = type,
        value = value,
        description = description)

    db.add(transaction)
    db.commit()
    return {"message": "Transação criada com sucesso"}

@app.delete("/financeira/{transaction_id}")
def delete_transaction(transaction_id: str):
  db = SessionLocal()
  transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

  if not transaction:
     return {"error": "Transação não encontrada"}

  db.delete(transaction)
  db.commit()
  return {"message": "Deletado com sucesso"}


@app.get("/relatorio")
def get_report():
    return system.generateReport()