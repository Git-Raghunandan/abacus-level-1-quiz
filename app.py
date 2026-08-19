if score == 10 and total == 10:

    # ====================================================
    # PERFECT SCORE CELEBRATION
    # ====================================================

    # Streamlit celebration
    st.balloons()

    # Extra celebration
    st.snow()

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px;
        ">

            <div style="
                font-size:48px;
                font-weight:bold;
            ">
                🎉🎉🎉
            </div>

            <div style="
                font-size:48px;
                font-weight:bold;
            ">
                PERFECT SCORE!
            </div>

            <div style="
                font-size:28px;
                margin-top:10px;
            ">
                🏆 YOU ARE A CHAMPION! 🏆
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ----------------------------------------------------
    # BIG TROPHY IMAGE
    # ----------------------------------------------------

    st.image(
        "images/trophy.png",
        width=350
    )

    # ----------------------------------------------------
    # SCORE
    # ----------------------------------------------------

    st.markdown(
        f"""
        <div style="
            text-align:center;
            margin-top:15px;
        ">

            <div style="
                font-size:60px;
                font-weight:bold;
            ">
                {score} / {total}
            </div>

            <div style="
                font-size:40px;
                font-weight:bold;
            ">
                💯 100%
            </div>

            <div style="
                font-size:35px;
                margin-top:15px;
            ">
                ⭐ ⭐ ⭐ ⭐ ⭐
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.success(
        f"🌟 AMAZING, {st.session_state.user_name}! "
        "You answered all 10 questions correctly!"
    )

    st.info(
        "🏆 PERFECT SCORE CHAMPION 🏆\n\n"
        "You have earned the Abacus Level 1 "
        "Perfect Score Trophy!"
    )
