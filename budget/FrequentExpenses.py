import matplotlib.pyplot as plt

import Expense
import collections

from Expense import Expenses



expenses = Expense.Expenses()

Expenses.read_expenses(expenses, "data/spending_data.csv")

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

fig,ax=plt.subplot()

ax.bar = (categories, count)

ax.set_title('# of Purchases by Category')

plt.show()
