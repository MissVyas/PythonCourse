print("Welcome to Roller Coaster Ride !!")
height = raw_input("Enter your height in cm: ")
bill = 0
if int(height) >= 120:
    age = int(raw_input(("Enter your age: ")))
    if age < 12:
        print("Child Pay 5$")
        bill=5
    elif 12 <= age <=18:
        print("Young Pay 7$")
        bill=7
    elif age < 45:
        print("Adults Pay 12$")
        bill=12
    elif age >= 45 and age <= 55 :
        print ("You can ride for free !!")
    needphotos = raw_input("Do you want photos. Press Y for yes and N for No: ")
    if needphotos == 'Y' and age < 45:
        print ("Photos will be taken!!")
        bill = bill + 3
        print ("Bill with phots will be: "+str(bill))
    elif 45 <= age <= 55 and needphotos == 'Y':
        print ("Photos will be taken for free !!")
    else:
        print ("Photos will not be taken!")
        print ("You bill remains !!"+str(bill))
    print("Enjoy your ride !!")
else:
    print("Sorry you need to be taller than 120 cm")