import random
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Abacus Level 1 Quiz",
    page_icon="🧮",
    layout="centered"
)


# ============================================================
# CUSTOM CSS - MOBILE FRIENDLY
# ============================================================

st.markdown(
    """
    <style>

    .main {
        max-width: 700px;
        margin: auto;
    }

    .quiz-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .quiz-subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 25px;
    }

    .question-box {
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #dddddd;
        text-align: center;
        margin: 20px 0;
    }

    .question-text {
        font-size: 34px;
        font-weight: bold;
    }

    .score-box {
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #dddddd;
        text-align: center;
        margin-top: 20px;
    }

    @media (max-width: 600px) {

        .quiz-title {
            font-size: 32px;
        }

        .quiz-subtitle {
            font-size: 17px;
        }

        .question-text {
            font-size: 30px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INITIALIZE SESSION STATE
# ============================================================

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "user_name" not in st.session_state:
    st.session_state.user_name = ""


# ============================================================
# QUESTION GENERATOR
# ============================================================

def generate_question(difficulty, operation):

    if difficulty == "Easy":
        minimum = 1
        maximum = 10

    elif difficulty == "Medium":
        minimum = 1
        maximum = 20

    else:
        minimum = 1
        maximum = 50

    num1 = random.randint(minimum, maximum)
    num2 = random.randint(minimum, maximum)

    # Choose operation
    if operation == "Addition":
        selected_operation = "+"

    elif operation == "Subtraction":
        selected_operation = "-"

    else:
        selected_operation = random.choice(["+", "-"])

    # Prevent negative answers
    if selected_operation == "-" and num2 > num1:
        num1, num2 = num2, num1

    if selected_operation == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2

    question = f"{num1} {selected_operation} {num2}"

    return question, answer


# ============================================================
# GENERATE UNIQUE QUESTIONS
# ============================================================

def generate_unique_questions(number_of_questions, difficulty, operation):

    questions = []
    used_questions = set()

    # Maximum possible attempts prevents an infinite loop
    maximum_attempts = number_of_questions * 100
    attempts = 0

    while len(questions) < number_of_questions:

        attempts += 1

        if attempts > maximum_attempts:
            break

        question, answer = generate_question(
            difficulty,
            operation
        )

        # IMPORTANT:
        # Only add a question if it has NOT been used
        if question not in used_questions:

            used_questions.add(question)

            questions.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

    return questions


# ============================================================
# GENERATE MULTIPLE CHOICE OPTIONS
# ============================================================

def generate_options(correct_answer):

    options = {correct_answer}

    # Create 3 different wrong answers
    while len(options) < 4:

        difference = random.randint(1, 5)

        if random.choice([True, False]):
            wrong_answer = correct_answer + difference
        else:
            wrong_answer = correct_answer - difference

        if wrong_answer >= 0:
            options.add(wrong_answer)

    options = list(options)

    random.shuffle(options)

    return options


# ============================================================
# START NEW QUIZ
# ============================================================

def start_new_quiz(
    number_of_questions,
    difficulty,
    operation
):

    questions = generate_unique_questions(
        number_of_questions,
        difficulty,
        operation
    )

    # Make sure enough unique questions were created
    if len(questions) < number_of_questions:

        st.error(
            "Unable to generate enough unique questions. "
            "Please reduce the number of questions or "
            "increase the difficulty."
        )

        return

    st.session_state.questions = questions

    st.session_state.current_question = 0

    st.session_state.score = 0

    st.session_state.answered = False

    st.session_state.last_result = None

    st.session_state.quiz_started = True


# ============================================================
# RESET QUIZ
# ============================================================

def reset_quiz():

    st.session_state.quiz_started = False

    st.session_state.questions = []

    st.session_state.current_question = 0

    st.session_state.score = 0

    st.session_state.answered = False

    st.session_state.last_result = None


# ============================================================
# HOME SCREEN
# ============================================================

if not st.session_state.quiz_started:

    st.markdown(
        '<div class="quiz-title">🧮 Abacus Level 1</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="quiz-subtitle">'
        'Math Practice Quiz'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # Student name
    name = st.text_input(
        "👧 Student Name",
        placeholder="Enter your name"
    )

    # Number of questions
    number_of_questions = st.selectbox(
        "📝 Number of Questions",
        [5, 10, 15, 20],
        index=1
    )

    # Difficulty
    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    # Operation
    operation = st.selectbox(
        "➕➖ Operation",
        [
            "Addition",
            "Subtraction",
            "Addition + Subtraction"
        ]
    )

    st.write("")

    if st.button(
        "🚀 START QUIZ",
        use_container_width=True
    ):

        if not name.strip():

            st.warning(
                "Please enter the student's name."
            )

        else:

            st.session_state.user_name = name.strip()

            start_new_quiz(
                number_of_questions,
                difficulty,
                operation
            )

            st.rerun()


# ============================================================
# QUIZ SCREEN
# ============================================================

else:

    questions = st.session_state.questions

    current_index = st.session_state.current_question

    total_questions = len(questions)

    # ========================================================
    # QUIZ COMPLETED
    # ========================================================

    if current_index >= total_questions:

        score = st.session_state.score

        percentage = (
            score / total_questions
        ) * 100

        st.markdown(
            '<div class="quiz-title">🎉 Quiz Complete!</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="score-box">',
            unsafe_allow_html=True
        )

        st.subheader(
            f"Well done, {st.session_state.user_name}! 🌟"
        )

        st.markdown(
            f"### Score: {score} / {total_questions}"
        )

        st.markdown(
            f"### Percentage: {percentage:.0f}%"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        # Performance message
        if percentage >= 90:

            st.success(
                "🏆 Outstanding! Excellent work!"
            )

        elif percentage >= 80:

            st.success(
                "🌟 Excellent! Keep it up!"
            )

        elif percentage >= 60:

            st.info(
                "👍 Good job! More practice will make you even better."
            )

        else:

            st.warning(
                "💪 Keep practicing. You can do it!"
            )

        st.write("")

        # Restart
        if st.button(
            "🔄 START NEW QUIZ",
            use_container_width=True
        ):

            reset_quiz()

            st.rerun()


    # ========================================================
    # CURRENT QUESTION
    # ========================================================

    else:

        question_data = questions[current_index]

        question = question_data["question"]

        correct_answer = question_data["answer"]

        # Generate options only once for this question
        options_key = f"options_{current_index}"

        if options_key not in st.session_state:

            st.session_state[options_key] = generate_options(
                correct_answer
            )

        options = st.session_state[options_key]

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        st.markdown(
            '<div class="quiz-title">🧮 Abacus Level 1</div>',
            unsafe_allow_html=True
        )

        st.write(
            f"👧 {st.session_state.user_name}"
        )

        # Progress
        st.progress(
            (current_index + 1) / total_questions
        )

        st.write(
            f"Question {current_index + 1} "
            f"of {total_questions}"
        )

        # ----------------------------------------------------
        # QUESTION
        # ----------------------------------------------------

        st.markdown(
            '<div class="question-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="question-text">'
            f'What is {question}?'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # ANSWERS
        # ----------------------------------------------------

        selected_answer = st.radio(
            "Choose your answer:",
            options,
            format_func=lambda x: f"{x}",
            key=f"answer_{current_index}"
        )

        st.write("")

        # ----------------------------------------------------
        # SUBMIT ANSWER
        # ----------------------------------------------------

        if not st.session_state.answered:

            if st.button(
                "✅ SUBMIT ANSWER",
                use_container_width=True
            ):

                if selected_answer == correct_answer:

                    st.session_state.score += 1

                    st.session_state.last_result = "correct"

                else:

                    st.session_state.last_result = "wrong"

                st.session_state.answered = True

                st.rerun()

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        else:

            if st.session_state.last_result == "correct":

                st.success(
                    "🎉 Correct! Great job!"
                )

            else:

                st.error(
                    f"❌ Not quite. "
                    f"The correct answer is {correct_answer}."
                )

            st.write("")

            if st.button(
                "➡️ NEXT QUESTION",
                use_container_width=True
            ):

                st.session_state.current_question += 1

                st.session_state.answered = False

                st.session_state.last_result = None

                st.rerun()
