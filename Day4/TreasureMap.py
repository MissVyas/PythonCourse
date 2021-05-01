# -*- coding: utf-8 -*-

row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]
map = [row1,row2,row3]
print(str(row1)+"\n"+str(row2)+"\n"+str(row3)+"\n")
position = raw_input("Where do you want to put the treasure?: ")
map[int(position[0])][int(position[1])] = 'x'
print(str(row1)+"\n"+str(row2)+"\n"+str(row3)+"\n")


