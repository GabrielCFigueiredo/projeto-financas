import _json
import json
import os

from app.database.database import SessionLocal
from app.models import Transaction
import matplotlib.pyplot as plt


class FinancialSystem:
    def __init__(self, db):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data = os.path.join(BASE_DIR, "data", "data.json")
        self.transactions = []
        self.db = db

    def addTransaction(self,type,value, description):

        db = SessionLocal()
        transaction = Transaction(
            type=type,
            value=value,
            description=description
        )

        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)

        return transaction

    def listTransactions(self):

        return self.db.query(Transaction).all()

    def listTransaction(self):
        return [t.to_dict() for t in self.transactions]

    def calculateBalance(self):
        balance = 0
        for t in self.transactions:
            if t.type == "receita":
                balance += t.value

            elif t.type == "despesa":
                balance -= t.value
        return balance

    def saveData(self):
        os.makedirs(os.path.dirname(self.data), exist_ok=True)

        with open(self.data, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=4)


    def filterRevenue(self):
        return [t.to_dict() for t in self.transactions if t.type == "receita"]

    def deleteTransaction(self,transaction_id):
        for t in self.transactions:
            if t.id == transaction_id:
                self.transactions.remove(t)
                self.saveData()
                return True
        return False

    def generateReport(self):
        total_revenue = 0
        total_expense = 0

        for t in self.transactions:
            value = float(t.value)

            if t.type == "receita":
                total_revenue += value
            elif t.type == "despesa":
                total_expense += value

        balance = total_revenue - total_expense

        return {
            "total_receitas": total_revenue,
            "total_despesas": total_expense,
            "saldo_final": balance,
            "quantidade_transacoes": len(self.transactions)
        }

    def generateChart(self):

        total_revenue = 0
        total_expense = 0

        for t in self.transactions:

            try:
                value = float(t.value)
            except ValueError:
                continue

            if t.type == "receita":
                total_revenue += value
            elif t.type == "despesa":
                total_expense += value

        labels = ["Receitas", "Despesas"]
        values = [total_revenue, total_expense]

        plt.bar(labels, values)

        plt.title("Relatório Financeiro")
        plt.ylabel("Valor (R$)")
        plt.xlabel("Tipo")

        plt.show()
        plt.savefig("relatorio.png")