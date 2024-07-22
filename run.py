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

      valid_input = False # Initialize a flag to indicate whether the input is valid
    while not valid_input: # Continue looping until valid input is provided
        
        #try used to catch errors from invalid inputs.
            try:
                answer = int(input("Enter the number of the correct answer: "))  # Prompt the user to enter the number of their chosen answer
                if 1 <= answer <= len(question.options):  # Ensure the answer is within the range of options
                    if question.options[answer - 1] == question.answer:
                        score += 1  # Increment score if the answer is correct
                    else:
                        incorrect_questions.append((question, answer))
                    valid_input = True # Set valid_input to True to exit the input loop
                else:
                    print("Please enter a valid number corresponding to one of the options.")
            except ValueError:
                print("Invalid input. Please enter a number corresponding to one of the options.")

    print(f"\nYou got {score} out of {len(questions)} correct!")  # Print the final score
    
    # Check if there are any incorrect answers
    if incorrect_questions:
        print("\nHere are the questions you answered incorrectly:")
        for question, given_answer in incorrect_questions:
            print(f"\nQuestion: {question.prompt}")
            print(f"Your answer: {given_answer if given_answer is not None else 'Invalid input'}")
            print(f"Correct answer: {question.answer}")
    
# Define the quiz questions
questions = [
    Question(
        "What is the chemical symbol for gold?",
        ["Au", "Ag", "Pb", "Pt"],
        "Au"
    ),
    Question(
        "Who invented the telephone?",
        ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"],
        "Alexander Graham Bell"
    ),
    Question(
        "Which planet is known for its beautiful rings?",
        ["Mars", "Venus", "Saturn", "Jupiter"],
        "Saturn"
    ),
    Question(
        "What year did the Titanic sink?",
        ["1912", "1905", "1898", "1923"],
        "1912"
    ),
    Question(
        "What is the rarest blood type?",
        ["A", "B", "AB-Negative", "O-Negative"],
        "AB-Negative"
    ),
    Question(
        "Who painted the ceiling of the Sistine Chapel?",
        ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
        "Michelangelo"
    ),
    Question(
        "What is the smallest planet in our solar system?",
        ["Mars", "Mercury", "Venus", "Pluto"],
        "Mercury"
    ),
    Question(
        "What is the tallest mountain in the world?",
        ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
        "Mount Everest"
    ),
    Question(
        "In which year did the Berlin Wall fall?",
        ["1989", "1975", "1991", "1961"],
        "1989"
    ),
    Question(
        "Who wrote 'Harry Potter'?",
        ["J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "Suzanne Collins"],
        "J.K. Rowling"
    )
]


    