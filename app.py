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
# MOBILE FRIENDLY CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        max-width: 700px;
        margin: auto;
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
    }

    .question-box {
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #dddddd;
        text-align: center;
        margin: 20px 0;
    }

    .question {
        font-size: 36px;
        font-weight: bold;
    }

    .trophy {
        text-align: center;
        font-size: 100px;
    }

    .perfect {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    .score {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
    }

    @media (max-width: 600px) {

        .title {
            font-size: 32px;
        }

        .question {
            font-size: 30px;
        }

        .perfect {
            font-size: 32px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "quiz_started": False,
    "questions": [],
    "current_question": 0,
    "score": 0,
    "answered": False,
    "last_result": None,
    "user_name": "",
    "options": {}
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# GENERATE ONE QUESTION
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

    if operation == "Addition":

        symbol = "+"

    elif operation == "Subtraction":

        symbol = "-"

    else:

        symbol = random.choice(["+", "-"])

    # Prevent negative answers
    if symbol == "-" and num2 > num1:

        num1, num2 = num2, num1

    if symbol == "+":

        answer = num1 + num2

    else:

        answer = num1 - num2

    question = f"{num1} {symbol} {num2}"

    return question, answer


# ============================================================
# GENERATE UNIQUE QUESTIONS
# ============================================================

def create_questions(number, difficulty, operation):

    questions = []

    used = set()

    attempts = 0

    max_attempts = number * 200

    while len(questions) < number:

        attempts += 1

        if attempts > max_attempts:
            break

        question, answer = generate_question(
            difficulty,
            operation
        )

        if question not in used:

            used.add(question)

            questions.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

    return questions


# ============================================================
# GENERATE OPTIONS
# ============================================================

def create_options(correct_answer):

    options = {correct_answer}

    while len(options) < 4:

        difference = random.randint(1, 5)

        if random.choice([True, False]):

            wrong = correct_answer + difference

        else:

            wrong = correct_answer - difference

        if wrong >= 0:

            options.add(wrong)

    options = list(options)

    random.shuffle(options)

    return options


# ============================================================
# START QUIZ
# ============================================================

def start_quiz(name, number, difficulty, operation):

    questions = create_questions(
        number,
        difficulty,
        operation
    )

    if len(questions) != number:

        st.error(
            "Could not generate enough unique questions. "
            "Please choose fewer questions or a higher difficulty."
        )

        return False

    st.session_state.quiz_started = True

    st.session_state.questions = questions

    st.session_state.current_question = 0

    st.session_state.score = 0

    st.session_state.answered = False

    st.session_state.last_result = None

    st.session_state.user_name = name

    st.session_state.options = {}

    return True


# ============================================================
# RESET
# ============================================================

def reset_quiz():

    st.session_state.quiz_started = False

    st.session_state.questions = []

    st.session_state.current_question = 0

    st.session_state.score = 0

    st.session_state.answered = False

    st.session_state.last_result = None

    st.session_state.user_name = ""

    st.session_state.options = {}


# ============================================================
# HOME PAGE
# ============================================================

if not st.session_state.quiz_started:

    st.markdown(
        '<div class="title">🧮 Abacus Level 1</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Math Quiz</div>',
        unsafe_allow_html=True
    )

    st.write("")

    name = st.text_input(
        "👧 Student Name",
        placeholder="Enter your name"
    )

    number = st.selectbox(
        "📝 Number of Questions",
        [5, 10, 15, 20],
        index=1
    )

    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Easy", "Medium", "Hard"]
    )

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

            success = start_quiz(
                name.strip(),
                number,
                difficulty,
                operation
            )

            if success:

                st.rerun()


# ============================================================
# QUIZ
# ============================================================

else:

    questions = st.session_state.questions

    current = st.session_state.current_question

    total = len(questions)


    # ========================================================
    # QUIZ COMPLETED
    # ========================================================

    if current >= total:

        score = st.session_state.score

        percentage = int(
            (score / total) * 100
        )


        # ====================================================
        # PERFECT 10/10
        # ====================================================

        if score == 10 and total == 10:

            st.balloons()

            st.markdown(
                '<div class="trophy">🏆</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="perfect">'
                'PERFECT SCORE!'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div style="text-align:center; '
                'font-size:28px;">'
                '🎉 Congratulations! 🎉'
                '</div>',
                unsafe_allow_html=True
            )

            st.write("")

            st.success(
                f"🌟 Amazing, "
                f"{st.session_state.user_name}!"
            )

            st.markdown(
                f'<div class="score">'
                f'{score} / {total}'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div style="text-align:center; '
                'font-size:35px; margin-top:10px;">'
                '💯 100%'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div style="text-align:center; '
                'font-size:30px; margin-top:15px;">'
                '⭐ ⭐ ⭐ ⭐ ⭐'
                '</div>',
                unsafe_allow_html=True
            )

            st.info(
                "🏅 You earned the "
                "Abacus Level 1 Perfect Score Trophy!"
            )


        # ====================================================
        # OTHER SCORES
        # ====================================================

        elif percentage >= 80:

            st.markdown(
                '<div style="text-align:center; '
                'font-size:80px;">🌟</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="perfect">'
                'Excellent Work!'
                '</div>',
                unsafe_allow_html=True
            )

            st.success(
                f"Great job, "
                f"{st.session_state.user_name}!"
            )

            st.metric(
                "Score",
                f"{score} / {total}"
            )

            st.metric(
                "Percentage",
                f"{percentage}%"
            )


        elif percentage >= 60:

            st.markdown(
                '<div style="text-align:center; '
                'font-size:70px;">👍</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="perfect">'
                'Good Job!'
                '</div>',
                unsafe_allow_html=True
            )

            st.info(
                "Keep practicing to reach 10/10!"
            )

            st.metric(
                "Score",
                f"{score} / {total}"
            )

            st.metric(
                "Percentage",
                f"{percentage}%"
            )


        else:

            st.markdown(
                '<div style="text-align:center; '
                'font-size:70px;">💪</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="perfect">'
                'Keep Practicing!'
                '</div>',
                unsafe_allow_html=True
            )

            st.warning(
                "Practice makes you better!"
            )

            st.metric(
                "Score",
                f"{score} / {total}"
            )

            st.metric(
                "Percentage",
                f"{percentage}%"
            )


        # ====================================================
        # NEW QUIZ
        # ====================================================

        st.write("")

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

        data = questions[current]

        question = data["question"]

        correct_answer = data["answer"]


        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        st.markdown(
            '<div class="title">🧮 Abacus Level 1</div>',
            unsafe_allow_html=True
        )

        st.write(
            f"👧 **{st.session_state.user_name}**"
        )

        st.progress(
            (current + 1) / total
        )

        st.write(
            f"Question **{current + 1}** of **{total}**"
        )


        # ----------------------------------------------------
        # QUESTION
        # ----------------------------------------------------

        st.markdown(
            '<div class="question-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="question">'
            f'What is {question}?'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # CREATE OPTIONS ONCE
        # ----------------------------------------------------

        if current not in st.session_state.options:

            st.session_state.options[current] = (
                create_options(correct_answer)
            )

        options = st.session_state.options[current]


        # ----------------------------------------------------
        # ANSWER
        # ----------------------------------------------------

        selected = st.radio(
            "Choose your answer:",
            options,
            key=f"answer_{current}"
        )


        st.write("")


        # ----------------------------------------------------
        # SUBMIT
        # ----------------------------------------------------

        if not st.session_state.answered:

            if st.button(
                "✅ SUBMIT ANSWER",
                use_container_width=True
            ):

                if selected == correct_answer:

                    st.session_state.score += 1

                    st.session_state.last_result = "correct"

                else:

                    st.session_state.last_result = "wrong"

                st.session_state.answered = True

                st.rerun()


        # ----------------------------------------------------
        # SHOW RESULT
        # ----------------------------------------------------

        else:

            if st.session_state.last_result == "correct":

                st.success(
                    "🎉 Correct! Great job!"
                )

            else:

                st.error(
                    f"❌ Wrong! "
                    f"The correct answer is "
                    f"{correct_answer}."
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
