import random


def generate_question():

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    operation = random.choice(["+", "-"])

    if operation == "+":

        answer = num1 + num2

    else:

        if num2 > num1:
            num1, num2 = num2, num1

        answer = num1 - num2

    question = f"{num1} {operation} {num2}"

    return question, answer


def generate_unique_question(used_questions):

    while True:

        question, answer = generate_question()

        if question not in used_questions:

            used_questions.add(question)

            return question, answer


def generate_options(correct_answer):

    options = {correct_answer}

    while len(options) < 4:

        offset = random.randint(-5, 5)

        wrong_answer = correct_answer + offset

        if wrong_answer >= 0:

            options.add(wrong_answer)

    options = list(options)

    random.shuffle(options)

    return options


def ask_question(question_number, question, correct_answer):

    options = generate_options(correct_answer)

    print()
    print(f"Question {question_number}")
    print("--------------------")
    print(f"What is {question}?")

    for index, option in enumerate(options):

        print(f"{chr(65 + index)}. {option}")

    while True:

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            break

        print("Please enter A, B, C or D.")

    selected_index = ord(user_answer) - ord("A")

    selected_answer = options[selected_index]

    if selected_answer == correct_answer:

        print("✅ Correct!")

        return True

    else:

        print(f"❌ Wrong! Correct answer is {correct_answer}.")

        return False


def start_quiz():

    print("=" * 40)
    print("       ABACUS LEVEL 1 QUIZ")
    print("=" * 40)

    while True:

        try:

            total_questions = int(
                input("How many questions do you want? ")
            )

            if total_questions > 0:
                break

            print("Enter a number greater than 0.")

        except ValueError:

            print("Please enter a valid number.")

    used_questions = set()

    score = 0

    for question_number in range(1, total_questions + 1):

        question, correct_answer = generate_unique_question(
            used_questions
        )

        result = ask_question(
            question_number,
            question,
            correct_answer
        )

        if result:
            score += 1

    percentage = (score / total_questions) * 100

    print()
    print("=" * 40)
    print("             RESULT")
    print("=" * 40)

    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {total_questions - score}")
    print(f"Percentage      : {percentage:.2f}%")

    if percentage >= 80:

        print("Excellent! 🌟")

    elif percentage >= 60:

        print("Good job! 👍")

    else:

        print("Keep practicing! 💪")


start_quiz()