import random

class Question: # Define the Question class
    def __init__(self, prompt, options, answer):
        """
        which takes one parameter questions. 
        This parameter is expected to be a list of Question objects.
        """
        self.prompt = prompt
        self.options = options
        self.answer = answer

