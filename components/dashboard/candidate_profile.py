"""
Premium Candidate Profile Dashboard.
"""

import streamlit as st

from components.ui.project_card import (
    render_project_card,
)

from services.skill_classifier import (
    SkillClassifier,
)

from components.ui.skill_chips import (
    render_skill_chips,
)

from components.ui.metric_card import (
    render_metric_card,
)

from components.ui.section_header import (
    render_section_header,
)


# ==========================================================
# Helpers
# ==========================================================


def _profile_completion(resume_data):
    """
    Calculate profile completeness.
    """

    info = resume_data.personal_info

    fields = [
        info.name,
        info.email,
        info.phone,
        resume_data.skills,
        resume_data.education,
        resume_data.experience,
        resume_data.projects,
        resume_data.certifications,
    ]

    completed = 0

    for field in fields:

        if isinstance(field, list):

            if field:
                completed += 1

        elif field:

            completed += 1

    return round(
        completed / len(fields) * 100
    )


# ==========================================================
# Education
# ==========================================================


def _render_education(items):

    st.subheader("🎓 Education")

    if not items:

        st.info("No education found.")

        return

    for edu in items:

        with st.container(border=True):

            st.markdown(
                f"### {edu.degree or 'Unknown Degree'}"
            )

            if edu.institution:

                st.caption(
                    edu.institution
                )

            years = []

            if edu.start_year:

                years.append(
                    edu.start_year
                )

            if edu.end_year:

                years.append(
                    edu.end_year
                )

            if years:

                st.write(
                    " - ".join(years)
                )

            if edu.cgpa:

                st.write(
                    f"CGPA : {edu.cgpa}"
                )


# ==========================================================
# Experience
# ==========================================================


def _render_experience(items):

    st.subheader("💼 Experience")

    if not items:

        st.info(
            "No experience found."
        )

        return

    for exp in items:

        with st.container(border=True):

            st.markdown(
                f"### {exp.role or exp.company}"
            )

            if exp.company:

                st.caption(
                    exp.company
                )

            if exp.duration:

                st.write(
                    exp.duration
                )

            if exp.description:

                st.write(
                    exp.description
                )


# ==========================================================
# Projects
# ==========================================================


def _render_projects(projects):

    st.subheader("🚀 Projects")

    if not projects:

        st.info(
            "No projects found."
        )

        return

    for project in projects:

        render_project_card(
            project,
        )

# ==========================================================
# String Lists
# ==========================================================


def _render_string_list(
    title,
    items,
    empty,
):

    st.subheader(title)

    if not items:

        st.info(empty)

        return

    for item in items:

        st.markdown(
            f"• {item}"
        )


# ==========================================================
# Main UI
# ==========================================================


def render_candidate_profile(
    resume_data,
):
    """
    Render premium candidate profile.
    """

    render_section_header(
        "👤 Candidate Profile",
        "Structured information extracted from the uploaded resume.",
    )

    info = resume_data.personal_info
    meta = resume_data.metadata

    completion = meta.get(
        "profile_completion",
        0,
    )

    # ======================================================
    # Profile Completion
    # ======================================================

    render_metric_card(
        "Profile Completion",
        f"{completion}%",
    )

    st.progress(
        completion / 100,
    )

    st.divider()

    # ======================================================
    # Top Section
    # ======================================================

    left, right = st.columns(
        [2, 1],
        gap="large",
    )

    # ------------------------------------------------------
    # Left
    # ------------------------------------------------------

    with left:

        st.subheader("📇 Personal Information")

        st.write(f"**Name:** {info.name or 'N/A'}")
        st.write(f"**Email:** {info.email or 'N/A'}")
        st.write(f"**Phone:** {info.phone or 'N/A'}")
        st.write(f"**Location:** {info.location or 'N/A'}")
        st.write(f"**LinkedIn:** {info.linkedin or 'N/A'}")
        st.write(f"**GitHub:** {info.github or 'N/A'}")

        st.divider()

        st.subheader("🧠 AI Resume Insights")

        st.write(
            f"**Primary Domain:** {meta.get('primary_domain','General')}"
        )

        st.write(
            f"**Profile Completion:** {completion}%"
        )

        st.write(
            f"**Skills Detected:** {meta.get('skill_count',0)}"
        )

        st.write(
            f"**Projects:** {meta.get('project_count',0)}"
        )

        st.write(
            f"**Experience Entries:** {meta.get('experience_count',0)}"
        )

    # ------------------------------------------------------
    # Right
    # ------------------------------------------------------

    with right:

        st.subheader("📊 Statistics")

        st.metric(
            "Skills",
            meta.get(
                "skill_count",
                0,
            ),
        )

        st.metric(
            "Projects",
            meta.get(
                "project_count",
                0,
            ),
        )

        st.metric(
            "Experience",
            meta.get(
                "experience_count",
                0,
            ),
        )

        st.metric(
            "Education",
            meta.get(
                "education_count",
                0,
            ),
        )

        st.metric(
            "Certificates",
            meta.get(
                "certification_count",
                0,
            ),
        )

    st.divider()

    # ======================================================
    # Skills
    # ======================================================

    st.subheader("🛠 Skills")

    categories = SkillClassifier.classify(
        resume_data.skills,
    )

    for category, skills in categories.items():

        if not skills:
            continue

        st.markdown(f"#### {category}")

        render_skill_chips(
            skills,
        )

    st.divider()

    # ======================================================
    # Education
    # ======================================================

    _render_education(
        resume_data.education,
    )

    st.divider()

    # ======================================================
    # Experience
    # ======================================================

    _render_experience(
        resume_data.experience,
    )

    st.divider()

    # ======================================================
    # Projects
    # ======================================================

    _render_projects(
        resume_data.projects,
    )

    st.divider()

    # ======================================================
    # Certifications
    # ======================================================

    _render_string_list(
        "🏆 Certifications",
        resume_data.certifications,
        "No certifications found.",
    )

    st.divider()

    # ======================================================
    # Languages
    # ======================================================

    _render_string_list(
        "🌍 Languages",
        resume_data.languages,
        "No languages found.",
    )

    st.divider()

    # ======================================================
    # Achievements
    # ======================================================

    _render_string_list(
        "🏅 Achievements",
        resume_data.achievements,
        "No achievements found.",
    )