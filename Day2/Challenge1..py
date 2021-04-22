num = raw_input("Enter Two digit number: ")
if 9 < int(num) < 100:
    str1 = str(num)
    sumofnum = int(str1[0])+int(str1[1])
    print "Sum of two digits in given number is: "+str(sumofnum)
else:
    raise Exception("Please enter in between 9 to 100")