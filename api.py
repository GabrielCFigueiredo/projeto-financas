from fastapi import FastAPI
from app.services import FinancialSystem

app = FastAPI()
system = FinancialSystem()

@app.get("/")
def home():
    return {"message": "API Financeira funcionando"}

@app.get("/financeira")
def get_transactions():
    return system.listTransaction()

@app.post("/financeira")
def create_transaction(type: str, description: str, value: float):
    system.addTransaction(type, value, description)
    return {"message": "Transação adicionada com sucesso"}

@app.delete("/financeira/{transaction_id}")
def delete_transaction(transaction_id: str):
  deleted =  system.deleteTransaction(transaction_id)
  if deleted:
     return {"message": "Transação removida com sucesso"}
  else:
     return  {"error": "ID não encontrado"}


@app.get("/relatorio")
def get_report():
    return system.generateReport()