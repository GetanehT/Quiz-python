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

    if incorrect_questions:
        print("\nHere are the questions you answered incorrectly:")
        for question, given_answer in incorrect_questions:
            print(f"\nQuestion: {question.prompt}")
            print(f"Your answer: {given_answer if given_answer is not None else 'Invalid input'}")
            print(f"Correct answer: {question.answer}")

# Define the quiz questions
questions = [
    Question(
        "What is the chemical symbol for hydrogen?",
        ["H", "He", "O", "N"],
        "H"
    ),
    Question(
        "What planet is known as the Earth's twin?",
        ["Mars", "Venus", "Jupiter", "Saturn"],
        "Venus"
    ),
    Question(
        "What is the hardest natural substance on Earth?",
        ["Gold", "Iron", "Diamond", "Platinum"],
        "Diamond"
    ),
    Question(
        "Who developed the theory of general relativity?",
        ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        "Albert Einstein"
    ),
    Question(
        "What is the largest organ in the human body?",
        ["Heart", "Liver", "Skin", "Brain"],
        "Skin"
    )

    ]

# Run the quiz
run_quiz(questions)
    
    