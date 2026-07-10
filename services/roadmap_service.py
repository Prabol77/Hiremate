from models.roadmap_model import (
    LearningRoadmap,
    LearningTask,
)


class RoadmapService:
    """
    Generate a personalized learning roadmap
    based on prioritized skill gaps.
    """

    ROADMAP_LIBRARY = {

        "docker": [
            "Learn Docker fundamentals",
            "Build Docker images",
            "Deploy a Dockerized application",
        ],

        "aws": [
            "Learn AWS EC2",
            "Understand IAM and S3",
            "Deploy an application on AWS",
        ],

        "kubernetes": [
            "Understand Kubernetes architecture",
            "Deploy pods and services",
            "Create a production deployment",
        ],

        "redis": [
            "Learn Redis basics",
            "Use Redis caching",
            "Integrate Redis into a project",
        ],

        "graphql": [
            "Learn GraphQL queries",
            "Build a GraphQL API",
            "Consume GraphQL in a frontend",
        ],
    }

    DEFAULT_PATH = [
        "Learn the fundamentals",
        "Practice with small exercises",
        "Build a mini project",
    ]

    def generate(
        self,
        skill_gap,
    ) -> LearningRoadmap:

        roadmap = LearningRoadmap()

        week = 1

        priority_groups = [

            skill_gap.high_priority,

            skill_gap.medium_priority,

            skill_gap.low_priority,

        ]

        for group in priority_groups:

            for gap in group:

                lessons = self.ROADMAP_LIBRARY.get(

                    gap.skill.lower(),

                    self.DEFAULT_PATH,

                )

                for lesson in lessons:

                    roadmap.tasks.append(

                        LearningTask(

                            week=week,

                            title=lesson,

                            description=f"Focus on {gap.skill}.",

                            estimated_hours=8,

                        )

                    )

                    week += 1

        roadmap.duration_weeks = max(
            week - 1,
            1,
        )

        return roadmap