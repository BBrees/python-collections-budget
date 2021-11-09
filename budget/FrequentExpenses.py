from . import Expense
import collections

import matplotlib.pyplot as plt

expenses = Expense.Expenses()

read_expenses(expenses, data/spending_data.csv)

spending_categories = []

for expense in expenses.list:
    append.expense_category(spending_categories)

spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

fig, ax = plt.subplot()

ax.bar(categories, count)

ax.set_title('# of Purchases by Category')

plt.show()
