student_heights = raw_input("Input a list of student heights ").split()
sum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum = sum+student_heights[n]
avg = round(sum/len(student_heights))
print avg
