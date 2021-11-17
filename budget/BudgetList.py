import Expense

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
    
def main():
    myBudgetList = budgetList.__init__(1200)
    expenses = Expense.Expense()
    expenses.read_expense("data/spending_data.csv")
    
    for expense in expenses.list:
        expense.amount.append(myBudgetList)

    print('The count of all expenses:', str(len(myBudgetList)))

if __name__ == "__main__":
    main()
