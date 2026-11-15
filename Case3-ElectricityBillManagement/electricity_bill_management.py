# Electricity Bill Management System

str_customer_name = input("Enter customer name: ")

int_units = int(input("Enter electricity units consumed: "))

if int_units <= 100:
    float_bill = int_units * 2

elif int_units <= 200:
    float_bill = (100 * 2) + ((int_units - 100) * 3)

else:
    float_bill = (100 * 2) + (100 * 3) + ((int_units - 200) * 5)

float_fixed_charge = 50

float_total_bill = float_bill + float_fixed_charge

print("\n--- ELECTRICITY BILL ---")
print("Customer Name:", str_customer_name)
print("Units Consumed:", int_units)
print("Electricity Charge: ₹", float_bill)
print("Fixed Charge: ₹", float_fixed_charge)
print("Total Bill: ₹", float_total_bill)
