import Expense

import matplotlib.pyplot as plt


class budgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    def append(self, item):
        if (self.sum_expenses + item) < self.budget:
            self.expenses.append(item)
        else:
            self.overages.append(item)

            return self.sum_overages + item
    
    def __len__(self):
        Sx = len(self.expenses)
        So = len(self.overages)

        return Sx + So
    
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)

        return self
    
    def __next__(self):
        try:
            return __next__(self.iter_e)
        except:
            StopIteration as stop
            return __next__(self.iter_o)
    
def main():
    myBudgetList = budgetList.__init__(1200)
    expenses = Expense.Expense()
    expenses.Expenses.read_expenses("data/spending_data.csv")
    
    for expense in expenses.list:
        expense.amount.append(myBudgetList)

    print('The count of all expenses:', str(len(myBudgetList)))

    for entry in myBudgetList:
        print(entry)
    
    fig, ax = plt.subplots()
    labels = 'Expenses', 'Overages', 'Budget'
    values = [myBudgetList: sum_expenses, sum_overages, budget]

    ax.bar(labels, values, color=['green', 'red', 'blue'])
    ax.set_title('Your total expense v. total budget')

    plt.show()


if __name__ == "__main__":
    main()
