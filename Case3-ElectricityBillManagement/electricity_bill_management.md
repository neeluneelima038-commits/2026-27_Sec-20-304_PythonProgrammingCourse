# Case Study 3 – Electricity Bill Management

## 1. Aim
To develop a Python program to calculate an electricity bill based on the number of units consumed.

## 2. INPUT
- Customer name.
- Number of electricity units consumed.

## 3. PROCESS
- Accept customer name and units consumed.
- Calculate the electricity bill based on unit rates.
- Add a fixed charge.
- Display the final bill.

## 4. OUTPUT
- Customer name.
- Units consumed.
- Electricity charge.
- Fixed charge.
- Total bill amount.

## 5. Algorithm
1. Start.
2. Enter customer name.
3. Enter electricity units consumed.
4. If units are less than or equal to 100, calculate the charge at ₹2 per unit.
5. If units are between 101 and 200, calculate the first 100 units at ₹2 and remaining units at ₹3.
6. If units are above 200, calculate the first 100 units at ₹2, the next 100 units at ₹3, and remaining units at ₹5.
7. Add a fixed charge of ₹50.
8. Display the electricity bill.
9. Stop.

## 6. Pseudocode
BEGIN
    READ str_customer_name
    READ int_units

    IF int_units <= 100 THEN
        SET float_bill = int_units * 2
    ELSE IF int_units <= 200 THEN
        SET float_bill = (100 * 2) + ((int_units - 100) * 3)
    ELSE
        SET float_bill = (100 * 2) + (100 * 3) + ((int_units - 200) * 5)
    END IF

    SET float_fixed_charge = 50
    SET float_total_bill = float_bill + float_fixed_charge

    DISPLAY str_customer_name
    DISPLAY int_units
    DISPLAY float_bill
    DISPLAY float_fixed_charge
    DISPLAY float_total_bill
END

## 7. Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[/Enter customer name and units/]
    B --> C{Units <= 100?}
    C -->|Yes| D[Calculate bill at ₹2 per unit]
    C -->|No| E{Units <= 200?}
    E -->|Yes| F[Calculate first 100 at ₹2 and remaining at ₹3]
    E -->|No| G[Calculate first 100 at ₹2, next 100 at ₹3 and remaining at ₹5]
    D --> H[Add fixed charge of ₹50]
    F --> H
    G --> H
    H --> I[/Display electricity bill/]
    I --> J([Stop])
