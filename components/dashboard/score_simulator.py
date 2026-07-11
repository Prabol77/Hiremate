import streamlit as st


def render_score_simulator(
    simulation,
):

    st.subheader(
        "📈 Hireability Score Simulator"
    )

    st.metric(
        "Current Score",
        f"{simulation.current_score}%",
    )

    st.divider()

    for action in simulation.actions:

        with st.container(border=True):

            st.markdown(
                f"### {action.title}"
            )

            st.write(
                action.description
            )

            st.metric(
                "Potential Score",
                f"{action.estimated_score}%",
                delta=f"+{action.score_gain}%",
            )

            st.caption(
                f"Difficulty: {action.difficulty}"
            )