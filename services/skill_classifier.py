"""
Skill Categorization Service.
"""


class SkillClassifier:

    CATEGORIES = {

        "💻 Programming": {

            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript",
        },

        "🌐 Web": {

            "HTML",
            "CSS",
            "Flask",
            "FastAPI",
            "REST API",
        },

        "🤖 AI / ML": {

            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "Scikit-Learn",
            "Pandas",
            "NumPy",
            "NLP",
            "LangChain",
            "Groq",
        },

        "🗄 Database": {

            "SQL",
            "MongoDB",
        },

        "☁ Cloud & DevOps": {

            "Docker",
            "AWS",
            "Azure",
            "Kubernetes",
        },

        "🛠 Tools": {

            "Git",
            "GitHub",
            "Linux",
            "Streamlit",
            "Plotly",
        },
    }

    @classmethod
    def classify(
        cls,
        skills,
    ):

        result = {
            category: []
            for category in cls.CATEGORIES
        }

        result["📦 Other"] = []

        for skill in skills:

            found = False

            for category, values in cls.CATEGORIES.items():

                if skill in values:

                    result[category].append(skill)

                    found = True

                    break

            if not found:

                result["📦 Other"].append(skill)

        return result