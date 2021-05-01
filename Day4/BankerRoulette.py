import random
string1 = raw_input("Enter the name of people seperated by comma and space")

list1 = string1.split(', ')

#choice = int(random.randint(0,len(list1)-1))

print random.choice(list1)