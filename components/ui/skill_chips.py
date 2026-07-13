"""
Neutral Skill Chips.
"""

import streamlit as st


def render_skill_chips(
    skills: list[str],
):
    """
    Render compact horizontal skill tags.
    """

    if not skills:
        st.caption("No skills found.")
        return

    html = '<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;margin-bottom:12px;">'

    for skill in skills:

        html += (
            f'<span style="'
            f'padding:6px 14px;'
            f'border-radius:999px;'
            f'background:#2b2b35;'
            f'border:1px solid #4b5563;'
            f'color:#ffffff;'
            f'font-size:13px;'
            f'font-weight:500;'
            f'white-space:nowrap;'
            f'display:inline-block;'
            f'">'
            f'{skill}'
            f'</span>'
        )

    html += "</div>"

    st.markdown(
        html,
        unsafe_allow_html=True,
    )