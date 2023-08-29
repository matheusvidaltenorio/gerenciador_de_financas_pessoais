from expense import Expense
from budget import Budget

class FinanceManager:
    def __init__(self):
        self.expenses = []
        self.budgets = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print("Despesa adicionada com sucesso.")

    def add_budget(self, category, amount):
        budget = Budget(category, amount)
        self.budgets.append(budget)
        print("Orçamento adicionado com sucesso.")

    def show_expenses(self):
        print("Despesas:")
        for expense in self.expenses:
            print(f"Valor: {expense.amount}, Categoria: {expense.category}, Descrição: {expense.description}")

    def show_budgets(self):
        print("Orçamentos:")
        for budget in self.budgets:
            print(f"Categoria: {budget.category}, Valor: {budget.amount}")


if __name__ == "__main__":
    finance_manager = FinanceManager()

    while True:
        print("\n1. Adicionar Despesa")
        print("2. Adicionar Orçamento")
        print("3. Mostrar Despesas")
        print("4. Mostrar Orçamentos")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            amount = float(input("Informe o valor da despesa: "))
            category = input("Informe a categoria da despesa: ")
            description = input("Informe a descrição da despesa: ")
            finance_manager.add_expense(amount, category, description)
        elif choice == '2':
            category = input("Informe a categoria do orçamento: ")
            amount = float(input("Informe o valor do orçamento: "))
            finance_manager.add_budget(category, amount)
        elif choice == '3':
            finance_manager.show_expenses()
        elif choice == '4':
            finance_manager.show_budgets()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")
