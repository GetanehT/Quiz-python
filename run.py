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
