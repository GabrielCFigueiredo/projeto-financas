import _json
import json
import os
from app.models import Transaction


class financialSystem:
    def __init__(self):
        self.transactions = []
        self.data = "data/data.json"
        self.loadData()

    def addTransaction(self,type,description,value):
        transaction = Transaction(type,description,value)
        self.transactions.append(transaction)
        self.saveData()

    def listTransaction(self):
        return [t.to_dict() for t in self.transactions]

    def calculateBalance(self):
        balance = 0
        for t in self.transactions:
            if t.type == "revenue":
                balance += t.value
            elif t.type == "expenses":
                balance += t.value
        return

    def saveData(self):
        with open(self.data,"r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

            for item in data:
                transactiom = Transaction(item["type"],item["description"],item["value"])
                self.transactions.append(transactiom)