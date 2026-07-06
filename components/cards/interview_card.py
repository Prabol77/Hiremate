import streamlit as st

from models.interview_model import InterviewResult


def render_interview_card(
    interview: InterviewResult,
) -> None:
    """
    Render AI-generated interview questions.

    Args:
        interview:
            AI interview preparation results.
    """

    st.header("🎤 AI Interview Preparation")

    # =====================================================
    # Questions
    # =====================================================

    if interview.questions:

        for (
            category,
            questions,
        ) in interview.questions.items():

            with st.expander(
                category,
                expanded=True,
            ):

                if questions:

                    for index, question in enumerate(
                        questions,
                        start=1,
                    ):

                        st.markdown(f"**{index}.** {question}")

                else:

                    st.info("No questions available.")

    else:

        st.info("No interview questions were generated.")

    # =====================================================
    # Tips
    # =====================================================

    if interview.overall_tips:

        st.divider()

        st.subheader("💡 Interview Tips")

        for tip in interview.overall_tips:

            st.success(tip)

    else:

        st.info("No interview tips available.")
