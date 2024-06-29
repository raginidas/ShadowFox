#Task 1:
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def determine_bmi_category(bmi):
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

def get_user_input():
    while True:
        try:
            height = float(input("Enter height in meters: "))
            if height <= 0:
                raise ValueError("Height must be greater than 0.")
            weight = float(input("Enter weight in kilograms: "))
            if weight <= 0:
                raise ValueError("Weight must be greater than 0.")
            return height, weight
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    print("Welcome to the BMI Calculator!")
    height, weight = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = determine_bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()
