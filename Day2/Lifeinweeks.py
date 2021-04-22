age = raw_input("What is your current age?")
remainingage = 90-int(age)
years = 365 * remainingage
weeks = 52 * remainingage
months = 12 * remainingage
print("You have "+str(years)+" years, "+str(weeks)+" week and "+str(months)+" month")