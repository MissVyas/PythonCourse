scores = raw_input("Input a list of scores ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

len_score = len(scores)
highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score

print highest_score



