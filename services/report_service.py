import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


class ReportService:
    """
    Generates a professional HireMate PDF report.
    """

    def __init__(self):
        self.styles = getSampleStyleSheet()

    # =====================================================
    # Helpers
    # =====================================================

    def _safe_text(self, value):
        """
        Prevent None crashes and ensure string output.
        """
        return str(value) if value is not None else "N/A"

    def _section(self, story, title):
        story.append(
            Paragraph(
                f"<b>{title}</b>",
                self.styles["Heading2"],
            )
        )
        story.append(Spacer(1, 8))

    def _bullet_list(self, story, items):
        """
        Safe bullet list renderer.
        """

        if not items:
            story.append(
                Paragraph(
                    "No data available.",
                    self.styles["BodyText"],
                )
            )
            story.append(Spacer(1, 8))
            return

        for item in items:
            story.append(
                Paragraph(
                    f"• {self._safe_text(item)}",
                    self.styles["BodyText"],
                )
            )

        story.append(Spacer(1, 10))

    # =====================================================
    # Main Generator
    # =====================================================

    def generate(
        self,
        output_path,
        resume_data,
        ats_result,
        review,
        recommendations,
        interview,
        cover_letter,
    ):
        """
        Generate PDF report.
        """

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True,
        )

        document = SimpleDocTemplate(output_path)
        story = []

        # ==================================================
        # Title
        # ==================================================

        story.append(
            Paragraph(
                "HireMate AI Resume Analysis Report",
                self.styles["Title"],
            )
        )

        story.append(
            Paragraph(
                datetime.now().strftime("Generated on %d %B %Y %H:%M"),
                self.styles["Italic"],
            )
        )

        story.append(Spacer(1, 20))

        # ==================================================
        # Candidate Info
        # ==================================================

        self._section(story, "Candidate Information")

        info = resume_data.personal_info

        story.append(
            Paragraph(f"Name: {self._safe_text(info.name)}", self.styles["BodyText"])
        )
        story.append(
            Paragraph(f"Email: {self._safe_text(info.email)}", self.styles["BodyText"])
        )
        story.append(
            Paragraph(f"Phone: {self._safe_text(info.phone)}", self.styles["BodyText"])
        )

        story.append(Spacer(1, 20))

        # ==================================================
        # ATS
        # ==================================================

        self._section(story, "ATS Analysis")

        score = getattr(ats_result, "overall_score", 0.0) or 0.0

        story.append(
            Paragraph(
                f"Overall Score: {float(score):.1f}%",
                self.styles["BodyText"],
            )
        )

        story.append(Spacer(1, 10))

        self._section(story, "Matched Skills")
        self._bullet_list(story, getattr(ats_result, "matched_skills", []))

        self._section(story, "Missing Skills")
        self._bullet_list(story, getattr(ats_result, "missing_skills", []))

        # ==================================================
        # Review
        # ==================================================

        self._section(story, "AI Resume Review")

        story.append(
            Paragraph(
                self._safe_text(getattr(review, "summary", "")),
                self.styles["BodyText"],
            )
        )

        story.append(Spacer(1, 10))

        self._section(story, "Strengths")
        self._bullet_list(story, getattr(review, "strengths", []))

        self._section(story, "Weaknesses")
        self._bullet_list(story, getattr(review, "weaknesses", []))

        # ==================================================
        # Recommendations
        # ==================================================

        self._section(story, "AI Recommendations")

        self._section(story, "ATS Optimization")
        self._bullet_list(story, getattr(recommendations, "ats_optimization", []))

        self._section(story, "Skills To Learn")
        self._bullet_list(story, getattr(recommendations, "skills_to_learn", []))

        self._section(story, "Resume Improvements")
        self._bullet_list(story, getattr(recommendations, "resume_improvements", []))

        self._section(story, "Next Steps")
        self._bullet_list(story, getattr(recommendations, "next_steps", []))

        # ==================================================
        # Interview
        # ==================================================

        self._section(story, "Interview Questions")

        questions = getattr(interview, "questions", {}) or {}

        for category, qlist in questions.items():
            self._section(story, category)
            self._bullet_list(story, qlist)

        self._section(story, "Interview Tips")
        self._bullet_list(
            story,
            getattr(interview, "overall_tips", []),
        )

        document.build(story)
