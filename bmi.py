# BMI = (weight in kg / height  in meters squared)
# Imperial version: BMI * 703

def  gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Metric or Imperial? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the Body Mass Index for the given weight,
    height and measurement system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system == 'imperial':
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        break
    elif system == 'metric':
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print(f"{system} is an invalid measurement system.")

 