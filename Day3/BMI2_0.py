height = raw_input("Enter your height in m: ")
weight = raw_input("Enter your weight in Kg: ")

bmi = round(float(weight)/float(height) ** 2)

print("Your BMI: "+str(bmi))

if bmi < 18.5 :
    print ("You are underweight!!")
elif 18.5 <= bmi < 25:
    print("You have normal weight!!")
elif 25 <= bmi < 30:
    print("You are overweight!!")
elif 30 <= bmi < 35:
    print("You are obese!!")
else:
    print("You are clinically obese")