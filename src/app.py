
DESTINATIONS = {
    "Chennai": ["Marina Beach", "Fort St. George"],
    "Ooty": ["Ooty Lake", "Botanical Garden"],
    "Madurai": ["Meenakshi Amman Temple"],
}

HOTELS = [
    {"name": "City Comfort", "location": "Chennai", "price": 1500},
    {"name": "Hill View", "location": "Ooty", "price": 2500},
    {"name": "Temple Stay", "location": "Madurai", "price": 1800},
]


def search_destinations(city):
    return DESTINATIONS.get(city, [])


def search_hotels(city):
    return [
        hotel for hotel in HOTELS
        if hotel["location"].lower() == city.lower()
    ]


def calculate_total(price_per_night, nights):
    if price_per_night < 0 or nights <= 0:
        raise ValueError("Invalid price or number of nights")
    return price_per_night * nights


if __name__ == "__main__":
    city = input("Enter destination: ")

    print("\nTourist attractions:")
    for place in search_destinations(city):
        print("-", place)

    print("\nHotels:")
    for hotel in search_hotels(city):
        print(f'{hotel["name"]} - Rs. {hotel["price"]}/night')
