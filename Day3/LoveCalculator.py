partnername = raw_input("Enter your partner name: ")
yourname = raw_input("Enter your name: ")

partnername = partnername.lower()
yourname = yourname.lower()

T_count = partnername.count('t') + yourname.count('t')
R_count = partnername.count('r') + yourname.count('r')
U_count = partnername.count('u') + yourname.count('u')
e_count = partnername.count('e') + yourname.count('e')

firstdigit = int(T_count) + int(R_count) + int(U_count) + int(e_count)

L_count = partnername.count('l') + yourname.count('l')
O_count = partnername.count('o') + yourname.count('o')
V_count = partnername.count('v') + yourname.count('v')
E_count = partnername.count('e') + yourname.count('e')

seconddigit = int(L_count) + int(O_count) + int(V_count) + int(E_count)

score = int(str(firstdigit)+str(seconddigit))

if score < 10 and score > 90:
    print("Your score is: "+str(score)+" You are like coke and mentos")
elif 40 <= score <= 50:
    print("Your score is: " + str(score) + " You are alright together!!")
else:
    print("Your score is: " + str(score))
