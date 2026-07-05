import streamlit as st


def render_skills_card(
    title: str,
    skills: list[str],
    status: str,
):
    """
    Render skills grid.
    """

    st.subheader(title)

    if not skills:

        st.info("None")

        return

    for skill in skills:

        if status == "success":

            st.success(skill)

        elif status == "error":

            st.error(skill)

        else:

            st.info(skill)