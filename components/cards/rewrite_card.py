import streamlit as st

from models.rewrite_model import RewriteResult


def render_rewrite_card(
    rewrite: RewriteResult,
):
    """
    Render AI Resume Rewrite results.
    """

    st.header("✨ AI Resume Rewrite")

    st.info(
        f"Section: {rewrite.section_name}"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Original")

        st.text_area(
            label="Original Resume Section",
            value=rewrite.original_text,
            height=250,
            disabled=True,
        )

    with col2:

        st.subheader("🚀 Improved")

        st.text_area(
            label="Improved Resume Section",
            value=rewrite.improved_text,
            height=250,
        )

    st.divider()

    st.subheader("🧠 Why this rewrite is better")

    st.success(
        rewrite.explanation
    )

    st.metric(
        "Estimated ATS Improvement",
        rewrite.estimated_improvement,
    )

    st.download_button(
        label="📄 Download Improved Section",
        data=rewrite.improved_text,
        file_name=f"{rewrite.section_name}_rewrite.txt",
        mime="text/plain",
        use_container_width=True,
    )