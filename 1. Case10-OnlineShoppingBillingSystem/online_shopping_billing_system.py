
# Case 10: Online Shopping Billing System
# Concepts: Lists, Loops and Calculations

list_product_names = []
list_product_prices = []
list_product_quantities = []
list_item_totals = []

int_count = int(input("Enter number of products: "))

for int_index in range(int_count):
    print("\nProduct", int_index + 1)

    str_product_name = input("Enter product name: ")
    float_product_price = float(input("Enter product price: "))
    int_quantity = int(input("Enter quantity: "))

    float_item_total = float_product_price * int_quantity

    list_product_names.append(str_product_name)
    list_product_prices.append(float_product_price)
    list_product_quantities.append(int_quantity)
    list_item_totals.append(float_item_total)

float_grand_total = sum(list_item_totals)

print("\n====== ONLINE SHOPPING BILL ======")

for int_index in range(int_count):
    print("Product:", list_product_names[int_index])
    print("Price:", list_product_prices[int_index])
    print("Quantity:", list_product_quantities[int_index])
    print("Total:", list_item_totals[int_index])
    print("----------------------------")

print("Grand Total: Rs.", float_grand_total)
print("Thank you for shopping!")
