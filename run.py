import random

class Question: # Define the Question class
    def __init__(self, prompt, options, answer):
       
        self.prompt = prompt
        self.options = options
        self.answer = answer
 # Define the run_quiz function
def run_quiz(questions):
    """
        which takes one parameter questions. 
        This parameter is expected to be a list of Question objects.
    """
    score = 0  
    incorrect_questions = []

random.shuffle(questions)  # Shuffle the questions to randomize their order

# Iterate through each question in the list of questions
for question in questions: 
    print(question.prompt) # Print the prompt for the current question
   
   # Iterate through each option for the current question
    for i, option in enumerate(question.options):
        print(f"{i + 1}. {option}")

    try:
        answer = int(input("Enter the number of the correct answer: "))
        if 1 <= answer <= len(question.options):  # Ensure the answer is within the range of options   
            if question.options[answer - 1] == question.answer:
              score += 1  # Increment score if the answer is correct
            else:
                 incorrect_questions.append((question, answer))
                 valid_input = True
        else:
             print("Please enter a valid number corresponding to one of the options.")