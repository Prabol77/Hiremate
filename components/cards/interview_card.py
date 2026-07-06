import streamlit as st

from models.interview_model import InterviewResult


def render_interview_card(
    interview: InterviewResult,
):
    """
    Render AI Interview Questions.
    """

    st.header("🎤 AI Interview Preparation")

    for category, questions in interview.questions.items():

        with st.expander(
            category,
            expanded=True,
        ):

            for index, question in enumerate(
                questions,
                start=1,
            ):

                st.markdown(
                    f"**{index}.** {question}"
                )

    if interview.overall_tips:

        st.divider()

        st.subheader("💡 Interview Tips")

        for tip in interview.overall_tips:

            st.success(tip)