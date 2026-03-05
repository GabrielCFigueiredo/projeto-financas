from app.services import FinancialSystem
from app.utils import showMenu


def main():
    system = FinancialSystem()

    while True:
        showMenu()
        option = input("Escolha uma opção: ")

        if option == "1":
            while True:
                try:
                    value = float(input("Valor da receita: "))
                    break
                except ValueError:
                    print("Digite apenas numeros.")
            description = input("Descrição: ")
            system.addTransaction("receita",value, description)

        elif option == "2":
            while True:
                try:
                    value = float(input("Valor da despesa: "))
                    break
                except ValueError:
                    print("Digite apenas numeros.")
            description = input("Descrição: ")
            system.addTransaction("despesa", value, description)


        elif option == "3":

            for t in system.listTransaction():
                print(f"""

        ID: {t['id']}

        Tipo: {t['type']}

        Descrição: {t['description']}

        Valor: {t['value']}

        -----------------------

        """)

        elif option == "4":
            print("Saldo atual:", system.calculateBalance())

        elif option == "5":
            transaction_id = input("Digite o ID da transação que deseja deletar: ")
            deleted = system.deleteTransaction(transaction_id)

            if deleted:
                print("Transação deletada com sucesso!")
            else:
                print("ID não encontrado.")

        elif option == "6":
            revenues = system.filterRevenue()

            if not revenues:
                print("Nenhuma receita encontrada.")
            else:
                for t in revenues:
                    print(f"""
        ID: {t['id']}
        Tipo: {t['type']}
        Descrição: {t['description']}
        Valor: {t['value']}
        -----------------------
        """)

        elif option == "7":
            report = system.generateReport()
            print("""
            ======== RELATÓRIO FINANCEIRO ========
            """)
            print(f"Total de Receitas: R$ {report['total_receitas']:.2f}")
            print(f"Total de Despesas: R$ {report['total_despesas']:.2f}")
            print(f"Saldo Final: R$ {report['saldo_final']:.2f}")
            print(f"Quantidade de Transações: {report['quantidade_transacoes']}")
            print("======================================")

        elif option == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")
if __name__ == "__main__":
    main()