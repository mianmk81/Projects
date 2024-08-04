from question import question

points = 0

fo = open('textfile.txt', 'r')
lines = fo.readlines()
fo.close()


for i in range(0, len(lines), 4):
    Question = lines[i]
    Answer = lines[i+1].split()
    print(Question)
    for j in range(len(Answer)):
        print("\t",Answer[j])
    print()
    answer = input("Enter Your Answer (A-D): ")
    print()