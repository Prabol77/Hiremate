import streamlit as st


def render_skills_card(title, skills, status="success"):
    """
    Display skill badges.
    """

    st.subheader(title)

    if not skills:

        st.warning("No skills found.")

        return

    cols = st.columns(3)

    for index, skill in enumerate(skills):

        col = cols[index % 3]

        if status == "success":
            col.success(skill)

        elif status == "error":
            col.error(skill)

        else:
            col.info(skill)