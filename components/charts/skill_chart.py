import plotly.graph_objects as go

import streamlit as st


def render_skill_chart(result):
    """
    Render ATS skill comparison.
    """

    figure = go.Figure()

    figure.add_trace(

        go.Bar(

            x=[
                "Matched",
                "Missing",
                "Additional",
            ],

            y=[
                len(result.matched_skills),
                len(result.missing_skills),
                len(result.additional_skills),
            ],
        )

    )

    figure.update_layout(

        title="Skill Comparison",

        height=350,

        xaxis_title="Category",

        yaxis_title="Count",
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
    )