#Task 2:
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
    country = city_to_country.get(normalized_city)
    return country

def main():
    city = input("Enter a city name: ")
    country = get_country_by_city(city)
    
    if country:
        print(f"{city} is in {country}")
    else:
        print(f"Sorry, the city {city} is not in the list.")

if __name__ == "__main__":
    main()
