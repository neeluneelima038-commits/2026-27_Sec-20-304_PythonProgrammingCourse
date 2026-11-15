# Case 53 – Food Waste Monitoring

## 1. Aim
To develop a Python program to monitor daily food
waste, calculate total and average waste, and
identify days with excessive food waste.

## 2. INPUT
- Number of monitoring days.
- Daily food waste in kilograms.
- Maximum acceptable waste limit.

## 3. PROCESS
- Accept daily food waste values.
- Calculate total food waste.
- Calculate average food waste.
- Compare daily waste with the given limit.
- Identify days with excessive food waste.

## 4. OUTPUT
- Total food waste.
- Average daily food waste.
- Days with excessive food waste.
- Food waste monitoring report.

## 5. Algorithm

1. Start.
2. Read the number of monitoring days.
3. Read the acceptable waste limit.
4. Read daily food waste values.
5. Calculate total food waste.
6. Calculate average food waste.
7. Compare each day's waste with the limit.
8. Store days exceeding the limit.
9. Display the results.
10. Stop.

## 6. Pseudocode

BEGIN

    READ int_days
    READ float_limit

    SET float_total = 0
    CREATE list_waste
    CREATE list_high_waste_days

    FOR each day

        READ float_waste
        ADD float_waste to list_waste
        ADD float_waste to float_total

        IF float_waste > float_limit THEN
            ADD day to list_high_waste_days
        END IF

    END FOR

    CALCULATE average_waste

    DISPLAY total_waste
    DISPLAY average_waste
    DISPLAY list_high_waste_days

END

## 7. Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Enter days and waste limit/]
    B --> C[Set total to zero and create lists]
    C --> D[/Enter daily waste/]
    D --> E[Add waste to total and list]
    E --> F{More days remaining?}
    F -- Yes --> D
    F -- No --> G[Calculate average waste]
    G --> H{Any day exceeds limit?}
    H -- Yes --> I[Identify high-waste days]
    H -- No --> J[/Display monitoring report/]
    I --> J
    J --> K([Stop])
