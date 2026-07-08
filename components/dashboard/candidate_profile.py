"""
Dashboard Candidate Profile.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)

from components.ui.status_badge import (
    render_status_badge,
)

from components.ui.metric_card import (
    render_metric_card,
)


def _render_list(
    title: str,
    items,
    empty_message: str,
):
    """
    Render lists for strings and dataclass objects.
    """

    st.subheader(title)

    if not items:

        render_status_badge(
            "info",
            empty_message,
        )

        st.divider()
        return

    for item in items:

        # -----------------------------------------
        # Plain strings (skills, certifications...)
        # -----------------------------------------

        if isinstance(item, str):

            st.markdown(f"• {item}")

        # -----------------------------------------
        # Education
        # -----------------------------------------

        elif hasattr(item, "degree"):

            st.markdown(f"• **{item.degree}**")

            if getattr(item, "institution", ""):

                st.caption(item.institution)

        # -----------------------------------------
        # Experience
        # -----------------------------------------

        elif hasattr(item, "company"):

            st.markdown(f"• **{item.company}**")

            role = getattr(item, "role", "")

            if role:

                st.caption(role)

        # -----------------------------------------
        # Project
        # -----------------------------------------

        elif hasattr(item, "title"):

            st.markdown(f"• **{item.title}**")

            description = getattr(
                item,
                "description",
                "",
            )

            if description:

                st.caption(description)

        else:

            st.write(item)

    st.divider()
def _profile_completion(
    resume_data,
) -> tuple[int, list[str]]:
    """
    Calculate profile completeness.
    """

    score = 0
    checks = []
    info=resume_data.personal_info
    fields = [
        ("Name", info.name),
        ("Email", info.email),
        ("Phone", info.phone),
        ("Skills", resume_data.skills),
        ("Education", resume_data.education),
        ("Projects", resume_data.projects),
        ("Experience", resume_data.experience),
        ("Certifications", resume_data.certifications),
    ]

    for title, value in fields:

        valid = False

        if isinstance(value, list):

            valid = len(value) > 0

        else:

            valid = bool(value)

        if valid:

            score += 1
            checks.append(f"✅ {title}")

        else:

            checks.append(f"⚠ Missing {title}")

    percentage = round(
        score / len(fields) * 100
    )

    return percentage, checks


def render_candidate_profile(
    resume_data,
):
    """
    Render candidate profile.
    """

    render_section_header(
        "👤 Candidate Profile",
        "Structured candidate information extracted from the resume.",
    )

    completion, checks = _profile_completion(
        resume_data,
    )

    render_metric_card(
        "Profile Completion",
        f"{completion}%",
    )

    st.progress(
        completion / 100,
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📇 Basic Information")

        info = resume_data.personal_info

        st.write(f"**Name:** {info.name or 'N/A'}")
        st.write(f"**Email:** {info.email or 'N/A'}")
        st.write(f"**Phone:** {info.phone or 'N/A'}")
        st.write(f"**Location:** {info.location or 'N/A'}")
        st.write(f"**LinkedIn:** {info.linkedin or 'N/A'}")
        st.write(f"**GitHub:** {info.github or 'N/A'}")

    with col2:

        st.subheader("📊 Profile Checks")

        for item in checks:

            st.write(item)

    st.divider()

    _render_list(
        "🛠 Skills",
        getattr(
            resume_data,
            "skills",
            [],
        ),
        "No skills detected.",
    )

    _render_list(
        "🎓 Education",
        getattr(
            resume_data,
            "education",
            [],
        ),
        "No education detected.",
    )

    _render_list(
        "💼 Experience",
        getattr(
            resume_data,
            "experience",
            [],
        ),
        "No experience detected.",
    )

    _render_list(
        "🚀 Projects",
        getattr(
            resume_data,
            "projects",
            [],
        ),
        "No projects detected.",
    )

    _render_list(
        "🏆 Certifications",
        getattr(
            resume_data,
            "certifications",
            [],
        ),
        "No certifications detected.",
    )