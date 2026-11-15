# Student Performance Analysis System

int_students = int(input("Enter number of students: "))

for int_student in range(1, int_students + 1):

    print("\nEnter Student Details")

    str_name = input("Enter student name: ")

    int_mark1 = int(input("Enter Subject 1 marks: "))
    int_mark2 = int(input("Enter Subject 2 marks: "))
    int_mark3 = int(input("Enter Subject 3 marks: "))

    int_total = int_mark1 + int_mark2 + int_mark3

    float_average = int_total / 3

    # Check pass or fail

    if int_mark1 >= 40 and int_mark2 >= 40 and int_mark3 >= 40:
        str_status = "PASS"
    else:
        str_status = "FAIL"

    # Assign grade

    if float_average >= 80:
        str_grade = "A"

    elif float_average >= 70:
        str_grade = "B"

    elif float_average >= 60:
        str_grade = "C"

    elif float_average >= 50:
        str_grade = "D"

    else:
        str_grade = "E"

    # Display report

    print("\n--- STUDENT PERFORMANCE REPORT ---")

    print("Student Name:", str_name)
    print("Total Marks:", int_total)
    print("Average Marks:", round(float_average, 2))
    print("Grade:", str_grade)
    print("Status:", str_status)
