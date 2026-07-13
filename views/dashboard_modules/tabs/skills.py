"""
Skills Dashboard Tab.

Responsibilities:
- Display matched skills
- Display missing skills
- Display skill statistics
"""

import streamlit as st

from models.ats_model import ATSResult


# ==========================================================
# Helper
# ==========================================================


def render_skill_chips(
    skills: list[str],
    color: str,
):
    """
    Render compact horizontal skill chips.
    """

    if not skills:

        st.info("None")

        return

    html = '<div style="display:flex; flex-wrap:wrap; gap:8px;">'

    for skill in skills:

        html += (
            f'<span style="'
            f'background:{color};'
            f'color:white;'
            f'padding:6px 14px;'
            f'border-radius:999px;'
            f'font-size:13px;'
            f'font-weight:600;'
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


# ==========================================================
# Skills Tab
# ==========================================================


def render_skills_tab(
    ats_result: ATSResult,
):
    """
    Render the Skills dashboard tab.
    """

    left, right = st.columns(2)

    # ======================================================
    # Matched Skills
    # ======================================================

    with left:

        st.subheader(
            "✅ Matched Skills"
        )

        render_skill_chips(
            ats_result.matched_skills,
            "#16a34a",
        )

    # ======================================================
    # Missing Skills
    # ======================================================

    with right:

        st.subheader(
            "❌ Missing Skills"
        )

        render_skill_chips(
            ats_result.missing_skills,
            "#d97706",
        )

    st.divider()

    # ======================================================
    # Statistics
    # ======================================================

    st.subheader(
        "📈 Skills Overview"
    )

    stat1, stat2, stat3 = st.columns(3)

    with stat1:

        st.metric(
            "Matched",
            len(
                ats_result.matched_skills
            ),
        )

    with stat2:

        st.metric(
            "Missing",
            len(
                ats_result.missing_skills
            ),
        )

    with stat3:

        total = (
            len(
                ats_result.matched_skills
            )
            + len(
                ats_result.missing_skills
            )
        )

        match_rate = (
            round(
                len(
                    ats_result.matched_skills
                )
                / total
                * 100,
            )
            if total
            else 100
        )

        st.metric(
            "Match Rate",
            f"{match_rate}%",
        )

    st.divider()

    st.caption(
        "Skills were automatically extracted by comparing your resume with the uploaded job description."
    )