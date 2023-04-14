questions = ["0) 1+1=", "1) 3-10=", "2) 12*7=", "3) 12:4=", "4) 15:9="]
answers = []
for i in range(5):
    answers.append(input())
x = 0
if int(answers[0]) == (1+1):
    x += 1
if int(answers[1]) == (3-10):
    x += 1
if int(answers[2]) == (12*7):
    x += 1
if int(answers[3]) == (12/4):
    x += 1
if float(answers[4]) == (15/9):
    x += 1
for i in range(5):
    print(questions[i] + str(answers[i]))
print(x)