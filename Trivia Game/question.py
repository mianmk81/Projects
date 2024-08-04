class question:
  """
  Question is a type of string ans1-ans4 is in a list of string of length 4 correct is the integer between 0 and 3
  """  
  def __init__(self, question, ans1, ans2, ans3, ans4, correct):
    self.question = question
    self.answers = []
    self.answers.append(ans1)
    self.answers.append(ans2)
    self.answers.append(ans3)
    self.answers.append(ans4)
    self.correct = correct
  
  def display(self):
    print(self.question)
    print("\tA.", self.answers[0])
    print("\tB.", self.answers[1])
    print("\tC.", self.answers[2])
    print("\tD.", self.answers[3])

  def check(self):
    valid = False
    answer = input("Enter Your Answer (A-D): ")
    while (not valid):
      valid = True
      if len(answer)  != 1:
        valid = False
      answer = answer.upper()
      if not answer in ["A", "B", "C", "D"]:
        valid = False
      if not valid:
        answer = input("Enter Your Answer (A-D): ")
    numAns = ord(answer) - ord('A')
    if numAns == self.correct:
      print("You are Correct")
      print("")
      return(True)
    else:
      print("You are Wrong")
      print("")
      return(False)

