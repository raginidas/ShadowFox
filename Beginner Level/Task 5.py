#Task 3:
def get_country_by_city(city):
    city_to_country = {
        "Sydney": "Australia",
        "Melbourne": "Australia",
        "Brisbane": "Australia",
        "Perth": "Australia",
        "Dubai": "UAE",
        "Abu Dhabi": "UAE",
        "Sharjah": "UAE",
        "Ajman": "UAE",
        "Mumbai": "India",
        "Bangalore": "India",
        "Chennai": "India",
        "Delhi": "India"
    }

    normalized_city = city.strip().title()
    return city_to_country.get(normalized_city)

def main():
    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")

    country1 = get_country_by_city(city1)
    country2 = get_country_by_city(city2)

    if country1 and country2:
        if country1 == country2:
            print(f"Both cities are in {country1}")
        else:
            print("They don't belong to the same country")
    else:
        if not country1:
            print(f"Sorry, the city {city1} is not in the list.")
        if not country2:
            print(f"Sorry, the city {city2} is not in the list.")

if __name__ == "__main__":
    main()
