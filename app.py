# ========================================================
# QUIZ COMPLETED
# ========================================================

if current_index >= total_questions:

    score = st.session_state.score

    percentage = (
        score / total_questions
    ) * 100

    # ----------------------------------------------------
    # PERFECT SCORE - 10/10
    # ----------------------------------------------------

    if score == total_questions and total_questions == 10:

        # Balloons
        st.balloons()

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:20px;
            ">

                <div style="font-size:90px;">
                    🏆
                </div>

                <div style="
                    font-size:42px;
                    font-weight:bold;
                ">
                    PERFECT SCORE!
                </div>

                <div style="
                    font-size:28px;
                    margin-top:10px;
                ">
                    🎉 Congratulations! 🎉
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            f"🌟 Amazing, {st.session_state.user_name}! "
            "You answered every question correctly!"
        )

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:25px;
                border:3px solid;
                border-radius:20px;
                margin:20px 0;
            ">

                <div style="font-size:24px;">
                    YOUR SCORE
                </div>

                <div style="
                    font-size:55px;
                    font-weight:bold;
                ">
                    {score} / {total_questions}
                </div>

                <div style="
                    font-size:35px;
                    font-weight:bold;
                ">
                    💯 100%
                </div>

                <div style="
                    font-size:25px;
                    margin-top:15px;
                ">
                    ⭐ ⭐ ⭐ ⭐ ⭐
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "🏅 You have earned the Abacus Level 1 "
            "Perfect Score Trophy!"
        )

    # ----------------------------------------------------
    # 80% OR ABOVE
    # ----------------------------------------------------

    elif percentage >= 80:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:20px;
            ">

                <div style="font-size:80px;">
                    🌟
                </div>

                <div style="
                    font-size:36px;
                    font-weight:bold;
                ">
                    Excellent Work!
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            f"Well done, {st.session_state.user_name}! "
            "Keep practicing!"
        )

        st.metric(
            "Your Score",
            f"{score} / {total_questions}"
        )

        st.metric(
            "Percentage",
            f"{percentage:.0f}%"
        )

    # ----------------------------------------------------
    # 60% OR ABOVE
    # ----------------------------------------------------

    elif percentage >= 60:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:20px;
            ">

                <div style="font-size:70px;">
                    👍
                </div>

                <div style="
                    font-size:32px;
                    font-weight:bold;
                ">
                    Good Job!
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "Good effort! Keep practicing to reach "
            "the perfect score."
        )

        st.metric(
            "Your Score",
            f"{score} / {total_questions}"
        )

        st.metric(
            "Percentage",
            f"{percentage:.0f}%"
        )

    # ----------------------------------------------------
    # BELOW 60%
    # ----------------------------------------------------

    else:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:20px;
            ">

                <div style="font-size:70px;">
                    💪
                </div>

                <div style="
                    font-size:32px;
                    font-weight:bold;
                ">
                    Keep Practicing!
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.warning(
            "Don't give up! Practice makes you better."
        )

        st.metric(
            "Your Score",
            f"{score} / {total_questions}"
        )

        st.metric(
            "Percentage",
            f"{percentage:.0f}%"
        )

    # ----------------------------------------------------
    # NEW QUIZ BUTTON
    # ----------------------------------------------------

    st.write("")

    if st.button(
        "🔄 START NEW QUIZ",
        use_container_width=True
    ):

        reset_quiz()

        st.rerun()
