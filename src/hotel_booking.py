
hotels = [
    {"name": "Green Valley Hotel", "city": "Coimbatore", "price": 2000, "available": True},
    {"name": "Royal Stay", "city": "Madurai", "price": 1500, "available": True},
    {"name": "City Comfort", "city": "Chennai", "price": 2500, "available": False},
]

def display_hotels():
    print("\n--- Available Hotels ---")
    for i, hotel in enumerate(hotels, start=1):
        status = "Available" if hotel["available"] else "Not Available"
        print(f"{i}. {hotel['name']} - {hotel['city']} - Rs.{hotel['price']}/night - {status}")

def book_hotel():
    display_hotels()

    try:
        choice = int(input("\nEnter hotel number to book: "))
        nights = int(input("Enter number of nights: "))

        if choice < 1 or choice > len(hotels):
            print("Invalid hotel number.")
            return

        if nights <= 0:
            print("Number of nights must be positive.")
            return

        hotel = hotels[choice - 1]

        if not hotel["available"]:
            print("Sorry, this hotel is not available.")
            return

        total = hotel["price"] * nights
        hotel["available"] = False

        print("\nBooking successful!")
        print("Hotel:", hotel["name"])
        print("City:", hotel["city"])
        print("Total cost: Rs.", total)

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    while True:
        print("\n=== Tourist Guide and Hotel Booking System ===")
        print("1. Display hotels")
        print("2. Book a hotel")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            display_hotels()
        elif option == "2":
            book_hotel()
        elif option == "3":
            print("Thank you for using our system!")
            break
        else:
            print("Invalid option. Try again.")
