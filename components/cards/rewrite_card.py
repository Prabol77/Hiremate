import streamlit as st

from models.rewrite_model import RewriteResult


def render_rewrite_card(
    rewrite: RewriteResult,
):
    """
    Render AI Resume Rewrite.
    """

    st.header("✨ AI Resume Rewrite")

    st.write("Compare your original resume content with the AI-improved version.")

    original_col, improved_col = st.columns(2)

    # ======================================================
    # Original
    # ======================================================

    with original_col:

        st.subheader("📄 Original")

        st.text_area(
            "",
            rewrite.original_text,
            height=220,
            disabled=True,
            key="original_resume",
        )

    # ======================================================
    # Improved
    # ======================================================

    with improved_col:

        st.subheader("🚀 AI Improved")

        st.text_area(
            "",
            rewrite.improved_text,
            height=220,
            disabled=True,
            key="improved_resume",
        )

    st.divider()

    st.subheader("💡 Why This Is Better")

    st.info(rewrite.explanation)

    st.metric(
        "Estimated ATS Improvement",
        rewrite.estimated_improvement,
    )
