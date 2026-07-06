import plotly.graph_objects as go
import streamlit as st

from models.ats_model import ATSResult


def render_skill_chart(
    result: ATSResult,
) -> None:
    """
    Render ATS skill comparison bar chart.

    Args:
        result:
            ATS analysis result.
    """

    matched = len(result.matched_skills or [])
    missing = len(result.missing_skills or [])
    additional = len(result.additional_skills or [])

    figure = go.Figure()

    figure.add_trace(
        go.Bar(
            x=[
                "Matched",
                "Missing",
                "Additional",
            ],
            y=[
                matched,
                missing,
                additional,
            ],
            marker_color=[
                "#22c55e",  # green
                "#ef4444",  # red
                "#3b82f6",  # blue
            ],
        )
    )

    figure.update_layout(
        title="Skill Comparison",
        height=350,
        xaxis_title="Category",
        yaxis_title="Count",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
    )
