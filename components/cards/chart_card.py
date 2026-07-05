import streamlit as st
import plotly.graph_objects as go


def render_skill_chart(ats_result):
    """
    Display a skill comparison donut chart.
    """

    values = [
        len(ats_result.matched_skills),
        len(ats_result.missing_skills),
        len(ats_result.additional_skills),
    ]

    labels = [
        "Matched",
        "Missing",
        "Additional",
    ]

    figure = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.6,
            )
        ]
    )

    figure.update_layout(
        title="Skill Distribution",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),
        height=350,
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
    )