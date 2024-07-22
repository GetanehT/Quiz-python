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
   
    for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")