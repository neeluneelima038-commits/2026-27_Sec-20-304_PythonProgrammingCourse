
# Case 7: Railway Ticket Reservation
# Concepts: Functions and Conditions

int_available_seats = 50
list_bookings = []

def book_ticket():
    global int_available_seats

    str_name = input("Enter passenger name: ")
    int_tickets = int(input("Enter number of tickets: "))

    if int_tickets > 0 and int_tickets <= int_available_seats:
        dict_booking = {
            "name": str_name,
            "tickets": int_tickets
        }

        list_bookings.append(dict_booking)
        int_available_seats -= int_tickets

        print("Ticket booked successfully!")
    else:
        print("Sorry! Tickets are not available.")

def display_bookings():
    if len(list_bookings) == 0:
        print("No bookings available.")
    else:
        print("\n--- Booking Details ---")
        for dict_booking in list_bookings:
            print("Passenger Name:", dict_booking["name"])
            print("Tickets:", dict_booking["tickets"])

    print("Available Seats:", int_available_seats)

while True:
    print("\n--- Railway Ticket Reservation ---")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Check Available Seats")
    print("4. Exit")

    int_choice = int(input("Enter your choice: "))

    if int_choice == 1:
        book_ticket()

    elif int_choice == 2:
        display_bookings()

    elif int_choice == 3:
        print("Available Seats:", int_available_seats)

    elif int_choice == 4:
        print("Thank you for using Railway Reservation System.")
        break

    else:
        print("Invalid choice. Please try again.")
