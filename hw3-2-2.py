# Ryan Lugo: RJL 10/6/21

height_feet = int(input("What's is your current height in feet?: "))
height_inches = int(input("What's your current height with inches?: "))
weight = int(input("What's your current weight in lbs?: "))

weight_convert = weight / 2.205

height_feet_to_inches = (height_feet * 12) + height_inches
height_convert = height_feet_to_inches / 39.37

bmi = weight_convert / (height_convert ** 2)

if bmi < 19:
    print("Underweight")
elif bmi < 25:
    print("Healthy")
elif bmi < 30:
    print("OverWeight")
elif bmi < 40:
    print("Obese")
elif bmi > 40:
    print("Extremely Obese")