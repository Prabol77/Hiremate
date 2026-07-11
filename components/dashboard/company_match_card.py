"""
Company Match Dashboard Card.
"""

import streamlit as st


# ==========================================================
# Company Match
# ==========================================================


def render_company_match_card(
    company_matches,
):
    """
    Render company compatibility analysis.
    """

    st.subheader(
        "🏢 Company Match Intelligence"
    )

    if not company_matches:

        st.info(
            "No company matches available."
        )

        return

    # ======================================================
    # Company Cards
    # ======================================================

    for company in company_matches:

        with st.container(
            border=True,
        ):

            st.markdown(
                f"## {company.company}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Overall Match",
                    f"{company.overall_match}%",
                )

                st.metric(
                    "Skill Match",
                    f"{company.skill_match}%",
                )

            with col2:

                st.metric(
                    "ATS Match",
                    f"{company.ats_match}%",
                )

                st.metric(
                    "Hireability",
                    f"{company.hireability_match}%",
                )

            st.success(
                company.recommendation,
            )

            if company.missing_skills:

                st.markdown(
                    "**Missing Skills**"
                )

                st.write(
                    ", ".join(
                        company.missing_skills,
                    )
                )

            else:

                st.success(
                    "No major skill gaps detected."
                )