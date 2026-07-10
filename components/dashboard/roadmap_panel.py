"""
Learning Roadmap Panel.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def render_roadmap_panel(
    roadmap,
):
    """
    Render weekly learning roadmap.
    """

    render_section_header(

        "🗺 Learning Roadmap",

        "A personalized plan to improve your resume and career readiness.",

    )

    st.metric(

        "Duration",

        f"{roadmap.duration_weeks} Weeks",

    )

    st.divider()

    if not roadmap.tasks:

        st.info(
            "No roadmap generated."
        )

        return

    for task in roadmap.tasks:

        with st.container(
            border=True,
        ):

            col1, col2 = st.columns(
                [1, 4]
            )

            with col1:

                st.metric(
                    "Week",
                    task.week,
                )

            with col2:

                st.markdown(
                    f"### {task.title}"
                )

                st.write(
                    task.description
                )

                st.caption(
                    f"Estimated Time: {task.estimated_hours} hrs"
                )