### THIS MIGHT HAPPEN EVERY ITERATION OF THE FOR LOOP, WINK WINK ###

# Show the user the question
# print(questions[index])

# Get the answer from the user
# userGuess = input()

# Compare the answer to the correct answer
# if(answer == answers[index])

#Title of Show
print("Welcome to Quiz-Mania!")
print()

#Rules of the Show
print(
    "Here is how the game is played. We give you 3 statements and you tell us if each one is True or False."
)
print()
print("If you get all 3 correct you WIN!")
print()
print("Simple Right?  Great, Now let's get the questions!")
print()
print(
    "Please remember to only answer each question with a T for True or a F for False"
)
print()
#Question Tuple
questions = (
    "#1. A rooster lays eggs. T or F: ",
    "#2. A pound of bricks is heavier than a pound of feathers. T or F: ",
    "#3. Tomatos are a Fruit. T or F: ")

#answer Tuple
answers = ("F", "F", "T")

# Calculate the number of questions
numberOfQuestions = len(questions)

#Ask Questions
#question = ""
right = 0


for index in range(numberOfQuestions):
  userAnswer = input(f"{questions[index]}")
  while userAnswer != "T" and userAnswer != "F":
    userAnswer = input(f"{questions[index]}")
  if(userAnswer == answers[index]):
    right += 1




# Tell the user how many they got right
print()
print(f"You got {right} right.")


#If they got all 3 right display message
if(right == 3):
  print("Congratulations! You got all 3 right and you are today's winner!")