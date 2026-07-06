import streamlit as st

STATUS_RENDERERS = {
    "success": st.success,
    "error": st.error,
    "info": st.info,
}


def render_skills_card(
    title: str,
    skills: list[str],
    status: str,
) -> None:
    """
    Render a categorized skills list.

    Args:
        title:
            Card title.

        skills:
            List of skills.

        status:
            Display style.
            Supported:
                - success
                - error
                - info
    """

    st.subheader(title)

    if not skills:

        st.info("No skills available.")

        return

    renderer = STATUS_RENDERERS.get(
        status,
        st.info,
    )

    for skill in sorted(skills):

        renderer(skill)
