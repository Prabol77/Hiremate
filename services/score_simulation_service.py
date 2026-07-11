"""
Hireability Score Simulation Service.
"""

from models.score_simulation_model import (
    ScoreSimulation,
    SimulationAction,
)


class ScoreSimulationService:
    """
    Simulates potential improvements to the
    candidate's Hireability Score.
    """

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        hireability,
        ats_result,
    ) -> ScoreSimulation:
        """
        Generate score improvement simulations.
        """

        simulation = ScoreSimulation()

        simulation.current_score = (
            hireability.overall
        )

        # ==================================================
        # Missing Skills
        # ==================================================

        for skill in ats_result.missing_skills[:3]:

            simulation.actions.append(

                SimulationAction(

                    title=f"Learn {skill}",

                    description=(
                        f"Gain practical experience in {skill}."
                    ),

                    score_gain=2,

                    estimated_score=min(
                        100,
                        simulation.current_score + 2,
                    ),

                    difficulty="Easy",

                )

            )

        # ==================================================
        # Portfolio Project
        # ==================================================

        simulation.actions.append(

            SimulationAction(

                title="Build a Portfolio Project",

                description=(
                    "Develop a real-world project showcasing your technical skills."
                ),

                score_gain=5,

                estimated_score=min(
                    100,
                    simulation.current_score + 5,
                ),

                difficulty="Medium",

            )

        )

        # ==================================================
        # Industry Certification
        # ==================================================

        simulation.actions.append(

            SimulationAction(

                title="Complete an Industry Certification",

                description=(
                    "Earn a certification relevant to your target role."
                ),

                score_gain=3,

                estimated_score=min(
                    100,
                    simulation.current_score + 3,
                ),

                difficulty="Medium",

            )

        )

        # ==================================================
        # Resume Optimization
        # ==================================================

        simulation.actions.append(

            SimulationAction(

                title="Optimize Resume Keywords",

                description=(
                    "Improve ATS compatibility by adding relevant keywords."
                ),

                score_gain=2,

                estimated_score=min(
                    100,
                    simulation.current_score + 2,
                ),

                difficulty="Easy",

            )

        )

        # ==================================================
        # Interview Preparation
        # ==================================================

        simulation.actions.append(

            SimulationAction(

                title="Practice AI Mock Interviews",

                description=(
                    "Improve technical and behavioral interview performance."
                ),

                score_gain=2,

                estimated_score=min(
                    100,
                    simulation.current_score + 2,
                ),

                difficulty="Easy",

            )

        )

        return simulation