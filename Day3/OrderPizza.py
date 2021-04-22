print("Welcome to Python Pizza Delivreies!!")
size = raw_input("What size pizza do you want ?? S, M or L ?? : ")
add_pepperoni = raw_input("Do you want pepporoni?? Y or N ?? : ")
extra_cheese = raw_input("Do you want extra cheese ?? Y or N ?? :")

bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == 'Y':
    bill = bill + 1

print("Your bill: $"+str(bill))