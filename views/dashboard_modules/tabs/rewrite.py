"""
Resume Rewrite Workspace.
"""

import streamlit as st


# ==========================================================
# Resume Rewrite Workspace
# ==========================================================


def render_rewrite_tab(
    rewrite,
):
    """
    Render the AI Resume Rewrite workspace.
    """

    st.title(
        "✨ AI Resume Rewrite"
    )

    st.caption(
        "Generate an ATS-optimized version of your resume while keeping all information truthful."
    )

    if rewrite is None:

        st.warning(
            "Resume rewrite is unavailable."
        )

        return

    # ======================================================
    # Professional Summary
    # ======================================================

    st.subheader(
        "📝 Professional Summary"
    )

    st.text_area(
        "",
        value=rewrite.professional_summary or "No summary generated.",
        height=160,
        disabled=True,
    )

    st.divider()

    # ======================================================
    # Experience
    # ======================================================

    st.subheader(
        "💼 Experience"
    )

    st.text_area(
        "",
        value=rewrite.experience or "No experience generated.",
        height=220,
        disabled=True,
    )

    st.divider()

# ======================================================
# Projects
# ======================================================

    st.subheader(
        "🚀 Projects"
    )

    projects_text = ""

    if isinstance(rewrite.projects, list):

        for project in rewrite.projects:

            if isinstance(project, dict):

                projects_text += (
                    f"• {project.get("project_name",project.get("name", ""))}\n"
                    f"  {project.get("project_description",project.get("description", ""))}\n\n"
                )

            else:

                projects_text += f"• {project}\n"

    else:

        projects_text = rewrite.projects or "No projects generated."

    st.text_area(
        "",
        value=projects_text,
        height=220,
        disabled=True,
    )
    st.divider()

# ======================================================
# Skills
# ======================================================

    st.subheader(
        "🛠 Optimized Skills"
    )

    if isinstance(rewrite.skills, list):

        skills_text = "\n".join(
            f"• {skill}"
            for skill in rewrite.skills
        )

    else:

        skills_text = rewrite.skills or "No skills generated."

    st.text_area(
        "",
        value=skills_text,
        height=180,
        disabled=True,
    )
    st.divider()

    # ======================================================
    # ATS Improvements
    # ======================================================

    st.subheader(
        "🎯 ATS Improvements"
    )

    st.success(
        rewrite.ats_improvement
        or "No ATS improvements available."
    )

    st.divider()

    # ======================================================
    # Suggestions
    # ======================================================

    st.subheader(
        "💡 AI Suggestions"
    )

    if rewrite.suggestions:

        for suggestion in rewrite.suggestions:

            st.markdown(
                f"✅ {suggestion}"
            )

    else:

        st.info(
            "No suggestions available."
        )

    st.divider()

    # ======================================================
    # Export
    # ======================================================

    st.subheader(
        "📄 Export"
    )

    rewritten_resume = f"""
=============================
HireMate AI Resume Rewrite
=============================

Professional Summary

{rewrite.professional_summary}


=================================

Experience

{rewrite.experience}


=================================

Projects

{rewrite.projects}


=================================

Skills

{rewrite.skills}


=================================

ATS Improvements

{rewrite.ats_improvement}


=================================

Suggestions

"""

    if rewrite.suggestions:

        for suggestion in rewrite.suggestions:

            rewritten_resume += (
                f"- {suggestion}\n"
            )

    st.download_button(
        label="📥 Export ATS-Optimized Resume",
        data=rewritten_resume,
        file_name="HireMate_Resume_Rewrite.txt",
        mime="text/plain",
        use_container_width=True,
    )