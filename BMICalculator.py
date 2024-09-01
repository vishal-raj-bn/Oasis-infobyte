def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (e.g., 70): "))
            if weight <= 0 or weight > 300:
                raise ValueError("Please enter a weight in a realistic range (0-300 kg).")
            
            height = float(input("Enter your height in meters (e.g., 1.75): "))
            if height <= 0 or height > 2.5:
                raise ValueError("Please enter a height in a realistic range (0-2.5 m).")
            
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()
