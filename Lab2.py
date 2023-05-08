def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)
    bmi = weight/(height**2)
    print("Your BMI is: ", bmi)
    if bmi < 18.5:
        print("You are underweight")
        return -1
    elif bmi > 25.0:
        print("You are overweight")
        return 1
    else:
        print("You are healthy")
        return 0