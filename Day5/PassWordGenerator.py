import string
import random
print("Welcome to the PyPassword Generator: ")
letters = raw_input("How many letters you want ? :")
numbers = raw_input("How many numbers you want? :")
symbols = raw_input("How many symbols? :")

len_password = int(letters)+int(numbers)+int(symbols)

password_list = []

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

number = range(0,10)
symbols_list = ['@','#','$','%','^','&']

i = 0

for char in range(1,int(letters)+1):
    password_list.append(random.choice(alphabet_list))

for char in range(1,int(numbers)+1):
    password_list.append(str(random.choice(number)))

for char in range(1,int(symbols)+1):
    password_list.append(str(random.choice(symbols_list)))

print password_list
random.shuffle(password_list)
print password_list

password = ""
for char1 in password_list:
    password += char1

print password




