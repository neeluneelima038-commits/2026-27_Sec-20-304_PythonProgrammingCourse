
# Case 5: Library Book Tracking System
# Concepts: Lists and Searching

list_books = []

while True:
    print("\n--- Library Book Tracking System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    int_choice = int(input("Enter your choice: "))

    if int_choice == 1:
        str_book = input("Enter book name: ")
        list_books.append(str_book)
        print("Book added successfully.")

    elif int_choice == 2:
        if len(list_books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for int_index, str_book in enumerate(list_books, start=1):
                print(int_index, ".", str_book)

    elif int_choice == 3:
        str_search_book = input("Enter book name to search: ")
        bool_found = False

        for str_book in list_books:
            if str_book.lower() == str_search_book.lower():
                print("Book found:", str_book)
                bool_found = True
                break

        if not bool_found:
            print("Book not found.")

    elif int_choice == 4:
        print("Thank you. Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
