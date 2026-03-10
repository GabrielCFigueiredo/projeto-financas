
import json
import os
from app.models import Transaction
import matplotlib.pyplot as plt


class FinancialSystem:
    def __init__(self, db):

        self.db = db

    def addTransaction(self,type,value, description):

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
            transactions = self.db.query(Transaction).all()
            return transactions

    def deleteTransaction(self,transaction_id):
        transaction = self.db.query(Transaction).filter(
            Transaction.id == transaction_id
        ).first()

        if not transaction:
            return False

        self.db.delete(transaction)
        self.db.commit()

        return True

    def generateReport(self):
        transactions = self.db.query(Transaction).all()

        total_revenue = 0
        total_expense = 0

        for t in transactions:

            if t.type == "receita":
                total_revenue += t.value

            elif t.type == "despesa":
                total_expense += t.value

        balance = total_revenue - total_expense

        return {
            "total_receitas": total_revenue,
            "total_despesas": total_expense,
            "saldo_final": balance,
            "quantidade_transacoes": len(transactions)
        }
