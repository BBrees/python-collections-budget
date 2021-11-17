import collections
import matplotlib.pyplot as plt

import Expense

expenses = Expense.Expenses()

expenses.read_expenses("data/spending_data.csv")

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)
top5 = spending_counter.most_common(5)
print ("number of categories = " + str(spending_counter.__len__()))

categories, count = zip(*top5)

fig,ax=plt.subplot()

ax.bar = (categories, count)

ax.set_title('# of Purchases by Category')

plt.show()
