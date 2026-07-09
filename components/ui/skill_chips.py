"""
Modern Skill Chips.
"""

import streamlit as st


def render_skill_chips(skills):

    if not skills:

        st.info(
            "No skills detected."
        )

        return

    html = ""

    for skill in skills:

        html += f"""
<span style="
display:inline-block;
padding:8px 16px;
margin:5px;
background:#262730;
border-radius:25px;
font-size:14px;
font-weight:600;
border:1px solid #444;
">
{skill}
</span>
"""

    st.markdown(
        html,
        unsafe_allow_html=True,
    )