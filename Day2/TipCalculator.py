print("Welcome to the tip calculator")
bill = raw_input("What was the total bill? : $")
people = raw_input("How many people to split the bill? :")
tip = raw_input("What percent of the tip would you like to give? 10, 12 or 15?: ")

tipamount = float(float(bill) * int(tip) / 100)
print tipamount
totalamount = float(bill)+float(tipamount)
eachpersontip = float(totalamount) / int(people)
print eachpersontip
print("Each person should pay $"+str(round(eachpersontip,2)))
