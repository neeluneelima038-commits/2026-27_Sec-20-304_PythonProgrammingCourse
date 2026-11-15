
# Case 6: Smart Water Usage Monitoring
# Concepts: Loops and Conditions

list_water_usage = []

int_days = int(input("Enter number of days: "))
float_limit = float(input("Enter daily water usage limit in litres: "))

for int_day in range(1, int_days + 1):
    float_usage = float(input("Enter water usage for day " + str(int_day) + ": "))
    list_water_usage.append(float_usage)

print("\n--- Water Usage Report ---")

for int_index, float_usage in enumerate(list_water_usage, start=1):
    print("Day", int_index, ":", float_usage, "litres")

    if float_usage > float_limit:
        print("Warning: Water usage exceeded the limit!")
    else:
        print("Water usage is within the limit.")

float_total = sum(list_water_usage)
float_average = float_total / int_days

print("\nTotal Water Usage:", float_total, "litres")
print("Average Daily Usage:", float_average, "litres")
print("Monitoring completed.")
