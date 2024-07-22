import random


class Question:
    """Define the Question class."""

    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer


def run_quiz(questions):
    """
    Function to run the quiz.
    Takes one parameter: questions, which is a list of Question objects.
    """
    score = 0
    incorrect_questions = []

    random.shuffle(questions)  # Shuffle the questions to randomize their order

    # Iterate through each question in the list of questions
    for question in questions:
        print(question.prompt)  # Print the prompt for the current question

        # Print each option with a number for user selection
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")

        valid_input = False  # Flag to track if input is valid

        while not valid_input:  # Loop until valid input is received
            try:
                answer = int(input("Enter the number of the correct answer: "))

                if 1 <= answer <= len(question.options):
                    if question.options[answer - 1] == question.answer:
                        score += 1  # Increment score if the answer is correct
                    else:
                        incorrect_questions.append((question, answer))

                    valid_input = True
                else:
                    print("Please enter a valid number to one of the options.")

            except ValueError:
                print("Invalid input.Please enter a number  to  the options.")

    # Print the final score
    print(f"\nYou got {score} out of {len(questions)} correct!")

    # Check if there are any incorrect answers
    if incorrect_questions:
        print("\nHere are the questions you answered incorrectly:")
        for question, given_answer in incorrect_questions:
            print(f"\nQuestion: {question.prompt}")
            print(f"Your answer: {given_answer if given_answer is not
                  None else 'Invalid input'}")
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
    ),
    Question(
        "Who was the first President of the United States?",
        ["Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
        "George Washington"
    ),
    Question(
        "In what year did the Titanic sink?",
        ["1905", "1912", "1920", "1935"],
        "1912"
    ),
    Question(
        "Who was the British Prime Minister during World War II?",
        ["Winston Churchill", "Chamberlain", "Attlee", "Harold Macmillan"],
        "Winston Churchill"
    ),
    Question(
        "Which empire was ruled by Genghis Khan?",
        ["Roman Empire", "Ottoman Empire", "Mongol Empire", "British Empire"],
        "Mongol Empire"
    ),
    Question(
        "What was the main cause of the American Civil War?",
        ["Taxation", "Slavery", "Territorial Expansion", "Trade Disputes"],
        "Slavery"
    )
]

print("Welcome to the Quiz!\n")
print("Test your knowledge with these questions.\n")

# Run the quiz
run_quiz(questions)
