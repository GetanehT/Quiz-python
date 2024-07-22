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
                answer = int(input("Enter the no of the correct answer:\n"))

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
        "What is the chemical symbol for hydrogen?\n",
        ["H", "He", "O", "N""\n"],
        "H"
    ),
    Question(
        "What planet is known as the Earth's twin?\n",
        ["Mars", "Venus", "Jupiter", "Saturn""\n"],
        "Venus"
    ),
    Question(
        "What is the hardest natural substance on Earth?\n",
        ["Gold", "Iron", "Diamond", "Platinum""\n"],
        "Diamond"
    ),
    Question(
        "Who developed the theory of general relativity?\n",
        ["Isaac Newto", "Albert Einstein", "Galilo Galili", "Nikol Tesla""\n"],
        "Albert Einstein"
    ),
    Question(
        "What is the largest organ in the human body?\n",
        ["Heart", "Liver", "Skin", "Brain""\n"],
        "Skin"
    ),
    Question(
        "Who was the first President of the United States?\n",
        ["Jefferson", "Abraham Lincol", "George Washington", "John Adams""\n"],
        "George Washington"
    ),
    Question(
        "In what year did the Titanic sink?\n",
        ["1905", "1912", "1920", "1935""\n"],
        "1912"
    ),
    Question(
        "Who was the British Prime Minister during World War II?\n",
        ["Winston Churchill", "Chamberlain", "Attlee", "Harold Macmillan""\n"],
        "Winston Churchill"
    ),
    Question(
        "Which empire was ruled by Genghis Khan?\n",
        ["Roman Empire", "Ottoman ", "Mongol Empire", "British Empire""\n"],
        "Mongol Empire"
    ),
    Question(
        "What was the main cause of the American Civil War?\n",
        ["Taxation", "Slavery", "Territorial Expansion", "Trade Disputes""\n"],
        "Slavery"
    )
]

print("Welcome to the Quiz!\n")
print("Test your knowledge with these questions.\n")

# Run the quiz
run_quiz(questions)
