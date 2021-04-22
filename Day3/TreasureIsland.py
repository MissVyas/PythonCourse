print('''
#########################################
__________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
#########################################
''')
print("Welcome to Treasure Island!!")
path1 = raw_input("Do you want to go left or right?:  ")

if path1.lower() == "right":
    print("Game Over!! Not right is always right !!")
else:
    path2 = raw_input("Do you want to swim or wait ? : ")
    if path2.lower() == "swim":
        print("Game Over!! There is no lake to swim")
    else:
        path3 = raw_input("There are three doors in front of you; which you want to select: Blue, Red or Yellow: ")
        if path3.lower() == "blue":
            print("Game over you cought by beasts!!")
        if path3.lower() == "red":
            print("Game over there is fire inside!!")
        if path3.lower() == "yellow":
            print("Congrates you win !!")
