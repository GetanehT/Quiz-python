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
    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        try:
            answer = int(input("Enter the number of the correct answer: "))
            if question.options[answer - 1] == question.answer:
                score += 1  # Increment score if the answer is correct
            else:
                incorrect_questions.append((question, answer))
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to one of the options.")
            incorrect_questions.append((question, None))
    
    print(f"\nYou got {score} out of {len(questions)} correct!")  # Print the final score
    
    