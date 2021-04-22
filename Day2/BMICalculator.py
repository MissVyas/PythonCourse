height = raw_input("Enter your height in m: ")
weight = raw_input("Enter your weight in Kg: ")

bmi = float(weight)/float(height) ** 2

print("Your BMI: "+str(int(bmi)))