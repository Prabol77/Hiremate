"""
Reusable Project Card.
"""

import streamlit as st

from components.ui.skill_chips import (
    render_skill_chips,
)


def render_project_card(project):
    """
    Render a project as a premium card.
    """

    with st.container(border=True):

        st.markdown(
            f"### 🚀 {project.title or 'Untitled Project'}"
        )

        if project.description:

            st.write(
                project.description
            )

        if project.technologies:

            st.markdown("**Technologies**")

            render_skill_chips(
                project.technologies,
            )