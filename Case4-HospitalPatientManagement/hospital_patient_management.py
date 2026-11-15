
# Case 4: Hospital Patient Management
# Concepts: Dictionaries and Lists

list_patients = []

while True:
    print("\n--- Hospital Patient Management ---")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Exit")

    int_choice = int(input("Enter your choice: "))

    if int_choice == 1:
        str_patient_id = input("Enter patient ID: ")

        if any(patient["patient_id"] == str_patient_id for patient in list_patients):
            print("Patient ID already exists.")
        else:
            str_name = input("Enter patient name: ")
            int_age = int(input("Enter patient age: "))
            str_disease = input("Enter disease: ")

            dict_patient = {
                "patient_id": str_patient_id,
                "name": str_name,
                "age": int_age,
                "disease": str_disease
            }

            list_patients.append(dict_patient)
            print("Patient added successfully.")

    elif int_choice == 2:
        if len(list_patients) == 0:
            print("No patient records available.")
        else:
            print("\n--- Patient Records ---")
            for dict_patient in list_patients:
                print("Patient ID:", dict_patient["patient_id"])
                print("Name:", dict_patient["name"])
                print("Age:", dict_patient["age"])
                print("Disease:", dict_patient["disease"])
                print("----------------------")

    elif int_choice == 3:
        str_search_id = input("Enter patient ID to search: ")
        bool_found = False

        for dict_patient in list_patients:
            if dict_patient["patient_id"] == str_search_id:
                print("\nPatient Found")
                print("Patient ID:", dict_patient["patient_id"])
                print("Name:", dict_patient["name"])
                print("Age:", dict_patient["age"])
                print("Disease:", dict_patient["disease"])
                bool_found = True
                break

        if not bool_found:
            print("Patient not found.")

    elif int_choice == 4:
        print("Thank you. Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
