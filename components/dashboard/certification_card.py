"""
Certification Dashboard Card.
"""

import streamlit as st


# ==========================================================
# Certification Intelligence
# ==========================================================


def render_certification_card(
    certifications,
):
    """
    Render certification recommendations.
    """

    st.subheader(
        "📜 Certification Intelligence"
    )

    if not certifications:

        st.info(
            "No certification recommendations available."
        )

        return

    # ======================================================
    # Certification Cards
    # ======================================================

    for certification in certifications:

        with st.container(
            border=True,
        ):

            st.markdown(
                f"### {certification.name}"
            )

            st.write(
                certification.description
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Provider",
                    certification.provider,
                )

            with col2:

                st.metric(
                    "Difficulty",
                    certification.difficulty,
                )

            with col3:

                st.metric(
                    "Duration",
                    certification.estimated_duration,
                )

            st.metric(
                "Expected Hireability Gain",
                f"+{certification.expected_score_gain}%",
            )

            st.markdown(
                "**Skills Covered**"
            )

            st.write(
                ", ".join(
                    certification.skills_covered,
                )
            )

            st.markdown(
                "**Target Companies**"
            )

            st.write(
                ", ".join(
                    certification.target_companies,
                )
            )

            st.success(
                f"Priority: {certification.priority}"
            )