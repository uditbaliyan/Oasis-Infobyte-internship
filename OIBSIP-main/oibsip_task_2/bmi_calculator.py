# BMI = (weight in pounds-lbs x 703) / (height in inches x height in inches or do height ** 2)
# if you're using weight in kilograms and height in meters, there's no need to multiply by 703

def get_user_input(prompt, input_type=float): #get_user_input is a helper function that simplifies the process of getting and validating user input while input_type parameter converts the user's input (initially a string) to a decimal number (float).
    while True:
        try:
            value = input_type(input(prompt))
            if value <= 0:
                raise ValueError #this statement is used to trigger an exception if the condition is not met
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 16.0:
        return "underweight (Severe Thinness)"
    elif 16.0 <= bmi < 17.0:
        return "underweight (Moderate Thinness)"
    elif 17.0 <= bmi < 18.5:
        return "underweight (Mild Thinness)"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight (Pre-obese)"
    elif 30.0 <= bmi < 35.0:
        return "Obesity (Class I)"
    elif 35.0 <= bmi < 40.0:
        return "Obesity (Class II)"
    else:
        return "Obesity (Class III)"

def bmi_calculator(): #this function contains the primary logic of the BMI program
    print("Welcome to the BMI Calculator")

    while True: #will break if the user chooses to exit the BMI program
        name = input("What is your name? ")
        print(f"Hello, {name}")
        
        weight = get_user_input("Enter your weight in kilograms: ") #prompts for and validates the user's weight.
        height = get_user_input("Enter your height in meters: ") #prompts for and validates the user's height.
        
        bmi = calculate_bmi(weight, height)
        bmi_category = classify_bmi(bmi)
        
        print(f"Your BMI is: {bmi:.2f}") #prints the BMI value formatted to 2 decimal places
        print(f"Dear {name}, you are classified as '{bmi_category}'")
        
        while True:
            exit_prompt = input("Do you want to calculate another BMI? (yes/no): ").strip().lower()
            if exit_prompt in ('yes', 'no' ,"y","n"):
                break
            print("Invalid input. Please enter 'yes - y' or 'no - n'.")
        
        if exit_prompt == 'no' or exit_prompt == 'n':
            print("Thank you for using the BMI Calculator. Goodbye!")
            break

if __name__ == "__main__": #condition checks if the script is being run directly. If it is, the block of code inside the if statement is executed, allowing the script to be used both as a standalone program and as an importable module
    bmi_calculator()
