from app.services import financialSystem
from app.utils import showMenu


def main():
    system = financialSystem()

    while True:
        showMenu()
        option = input("Escolha uma opção: ")

        if option == "1":
            value = float(input("Valor da receita: "))
            description = input("Descrição: ")
            system.addTransaction("receita", value, description)

        elif option == "2":
            value = float(input("Valor da despesa: "))
            description = input("Descrição: ")
            system.addTransaction("despesa", value, description)

        elif option == "3":
            for t in system.listTransaction():
                print(t)

        elif option == "4":
            print("Saldo atual:", system.calculateBalance())

        elif option == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()