'''
- list of questions and answers for the trivia game
- store the answers
- randomly pick questions
- ask the questions
- see of they are correct
- keep track of score
- tell the user their score at the end

'''

questions = {
    "What is a correct syntax to output 'Hello World' in Python?" : "print('Hello World')",
    "How do you insert COMMENTS in Python code?" : "#This is a comment",
    "What is the correct file extension for Python files?" : ".py",
    "How do you create a variable with the numeric value 5?" : "x = 5",
    "How do you create a variable with the floating number 2.8?" : "x = 2.8",
    "Which method can be used to remove any whitespace from both the beginning and the end of a string?" : "strip()",
    "What is the correct way to create a function in Python?" : "def my_function():",
    "In Python, 'Hello', is the same as 'Hello'" : "True",
    "What is the correct way to create a class in Python?" : "class MyClass:",
    "What is the correct syntax to return the first character in a string?" : "x[0]",
    "Which method can be used to return a string in upper case letters?" : "upper()",
    "Which method can be used to return a string in lower case letters?" : "lower()",
    "Which method can be used to replace parts of a string?" : "replace()",
    "Which operator can be used to compare two values?" : "==",
    "Which of the following is a Python tuple?" : "(1, 2, 3)"
}

import random as rd

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = rd.sample(questions_list, total_questions)
    print(selected_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question].lower()
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {questions[question]}.\n")

    print(f"Your final score is: {score}/{total_questions}")

python_trivia_game()