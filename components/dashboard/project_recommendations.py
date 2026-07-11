"""
Project Recommendations Card.
"""

import streamlit as st


# ==========================================================
# Project Recommendations
# ==========================================================


def render_project_recommendations(
    projects,
):
    """
    Render recommended portfolio projects.
    """

    st.subheader(
        "🚀 Recommended Portfolio Projects"
    )

    if not projects:

        st.info(
            "No project recommendations available."
        )

        return

    # ======================================================
    # Project Cards
    # ======================================================

    for project in projects:

        with st.container(
            border=True,
        ):

            st.markdown(
                f"### {project.title}"
            )

            st.write(
                project.description
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Difficulty",
                    project.difficulty,
                )

            with col2:

                st.metric(
                    "Duration",
                    project.estimated_duration,
                )

            with col3:

                st.metric(
                    "Hireability Gain",
                    f"+{project.expected_score_gain}%",
                )

            st.markdown(
                "**Technologies**"
            )

            st.write(
                ", ".join(
                    project.technologies,
                )
            )

            if project.skills_covered:

                st.markdown(
                    "**Skills Covered**"
                )

                st.write(
                    ", ".join(
                        project.skills_covered,
                    )
                )

            if project.priority:

                st.success(
                    f"Priority: {project.priority}"
                )