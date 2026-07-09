"""
Resume Strength Dashboard.
"""

from components.ui.section_header import (
    render_section_header,
)

from components.ui.progress_bar import (
    render_progress_bar,
)


def render_resume_strength(
    resume_data,
    ats_result,
):
    """
    Render dynamic resume strength analysis.
    """

    render_section_header(
        "📈 Resume Strength",
        "Overall quality of the uploaded resume.",
    )

    # ==========================================
    # ATS Score
    # ==========================================

    ats_score = ats_result.overall_score

    # ==========================================
    # Skill Match
    # ==========================================

    matched = len(
        ats_result.matched_skills
    )

    missing = len(
        ats_result.missing_skills
    )

    total = max(
        matched + missing,
        1,
    )

    skill_score = (
        matched / total
    ) * 100

    # ==========================================
    # Profile Completeness
    # ==========================================

    sections = [

        resume_data.personal_info.name,

        resume_data.personal_info.email,

        resume_data.personal_info.phone,

        resume_data.skills,

        resume_data.education,

        resume_data.experience,

        resume_data.projects,

        resume_data.certifications,
    ]

    completed = 0

    for section in sections:

        if isinstance(section, list):

            if section:

                completed += 1

        elif section:

            completed += 1

    completeness = (
        completed / len(sections)
    ) * 100

    # ==========================================
    # Experience Score
    # ==========================================

    experience_score = min(
        len(resume_data.experience) * 25,
        100,
    )

    # ==========================================
    # Project Score
    # ==========================================

    project_score = min(
        len(resume_data.projects) * 20,
        100,
    )

    # ==========================================
    # Render
    # ==========================================

    render_progress_bar(
        "ATS Score",
        ats_score,
    )

    render_progress_bar(
        "Skill Match",
        skill_score,
    )

    render_progress_bar(
        "Profile Completeness",
        completeness,
    )

    render_progress_bar(
        "Experience Strength",
        experience_score,
    )

    render_progress_bar(
        "Project Portfolio",
        project_score,
    )