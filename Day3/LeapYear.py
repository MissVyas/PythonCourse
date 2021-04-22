year = int(raw_input("Which year do you want to check? "))

if (year%4 == 0) and (year%400 == 0):
    print ("Year is a leap year")
elif (year%4 == 0) and not ("year%100 == 0"):
    print ("This is not a leap year")
else:
    print("Year is not a leap year!")