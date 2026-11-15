
# Case 9: Employee Salary Management
# Concepts: Functions and Operators

def calculate_salary(float_basic):
    float_allowance = float_basic * 0.20
    float_bonus = float_basic * 0.10
    float_deduction = float_basic * 0.05

    float_net_salary = float_basic + float_allowance + float_bonus - float_deduction

    return float_allowance, float_bonus, float_deduction, float_net_salary


def display_salary():
    str_name = input("Enter employee name: ")
    float_basic = float(input("Enter basic salary: "))

    float_allowance, float_bonus, float_deduction, float_net_salary = calculate_salary(float_basic)

    print("\n--- Employee Salary Details ---")
    print("Employee Name:", str_name)
    print("Basic Salary:", float_basic)
    print("Allowance:", float_allowance)
    print("Bonus:", float_bonus)
    print("Deduction:", float_deduction)
    print("Net Salary:", float_net_salary)


int_count = int(input("Enter number of employees: "))

for int_index in range(int_count):
    print("\nEmployee", int_index + 1)
    display_salary()

print("\nSalary calculation completed.")
