import streamlit as st


def render_skills_card(
    title,
    skills,
    status="success",
):
    """
    Render skills list.
    """

    st.subheader(title)

    if not skills:

        st.warning("No skills found.")

        return

    cols = st.columns(2)

    for index, skill in enumerate(skills):

        column = cols[index % 2]

        if status == "success":

            column.success(skill)

        elif status == "error":

            column.error(skill)

        else:

            column.info(skill)