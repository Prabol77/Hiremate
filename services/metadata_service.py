"""
Resume Metadata Service.
"""

from collections import Counter


class MetadataService:
    """
    Generates computed metadata for ResumeData.
    """

    DOMAIN_MAP = {

        "AI/ML": {
            "Python",
            "TensorFlow",
            "Scikit-Learn",
            "NLP",
            "Deep Learning",
            "Machine Learning",
            "LangChain",
            "Groq",
        },

        "Web Development": {
            "HTML",
            "CSS",
            "JavaScript",
            "Flask",
            "FastAPI",
        },

        "Data Science": {
            "Pandas",
            "NumPy",
            "SQL",
            "Plotly",
        },

        "DevOps": {
            "Docker",
            "Linux",
            "AWS",
            "Kubernetes",
        },
    }

    def generate(
        self,
        resume,
    ):

        metadata = {}

        metadata["skill_count"] = len(
            resume.skills
        )

        metadata["project_count"] = len(
            resume.projects
        )

        metadata["experience_count"] = len(
            resume.experience
        )

        metadata["education_count"] = len(
            resume.education
        )

        metadata["certification_count"] = len(
            resume.certifications
        )

        metadata["profile_completion"] = (
            self.profile_completion(
                resume
            )
        )

        metadata["primary_domain"] = (
            self.detect_domain(
                resume.skills
            )
        )

        return metadata

    # ============================================

    def profile_completion(
        self,
        resume,
    ):

        fields = [

            resume.personal_info.name,

            resume.personal_info.email,

            resume.personal_info.phone,

            resume.skills,

            resume.education,

            resume.projects,

            resume.experience,

            resume.certifications,

        ]

        completed = 0

        for field in fields:

            if isinstance(
                field,
                list,
            ):

                if field:

                    completed += 1

            elif field:

                completed += 1

        return round(
            completed / len(fields) * 100
        )

    # ============================================

    def detect_domain(
        self,
        skills,
    ):

        counter = Counter()

        for skill in skills:

            for domain, values in self.DOMAIN_MAP.items():

                if skill in values:

                    counter[domain] += 1

        if not counter:

            return "General"

        return counter.most_common(1)[0][0]