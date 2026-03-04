import _json
import json
import os
from app.models import Transaction


class FinancialSystem:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data = os.path.join(BASE_DIR, "data", "data.json")
        self.transactions = []
        self.loadData()

    def addTransaction(self,type,value, description):
        transaction = Transaction(type,value, description)
        if value > 0:
            self.transactions.append(transaction)
            self.saveData()

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

    def loadData(self):
        if not os.path.exists(self.data):
            return
        with open(self.data,"r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

            for item in data:
                transaction = Transaction(item["type"], item["description"], item["value"],item.get("id"))
                self.transactions.append(transaction)

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
            if t.type == "receita":
                total_revenue += t.value
            elif t.type == "despesa":
                total_expense += t.value

        balance = total_expense - total_revenue
        return{
            "Total de Receitas": total_revenue,
            "Total de Expenses": total_expense,
            "Saldo Final": balance,
            "Quantidade de Transações": len(self.transactions)
        }