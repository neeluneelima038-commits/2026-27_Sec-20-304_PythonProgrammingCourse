
# Case 8: Personal Expense Tracker
# Concepts: Lists and Calculations

list_expenses = []
list_amounts = []

int_count = int(input("Enter number of expenses: "))

for int_index in range(int_count):
    str_name = input("Enter expense name: ")
    float_amount = float(input("Enter expense amount: "))

    list_expenses.append(str_name)
    list_amounts.append(float_amount)

print("\n--- Personal Expense Report ---")

for int_index in range(int_count):
    print(list_expenses[int_index], ":", list_amounts[int_index])

float_total = sum(list_amounts)

if int_count > 0:
    float_average = float_total / int_count
else:
    float_average = 0

print("\nTotal Expenses:", float_total)
print("Average Expense:", float_average)
print("Expense tracking completed.")
