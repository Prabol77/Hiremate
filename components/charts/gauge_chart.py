import plotly.graph_objects as go
import streamlit as st


def render_gauge(
    score: float,
) -> None:
    """
    Render the ATS Match Score gauge chart.

    Args:
        score:
            ATS score between 0 and 100.
    """

    score = max(
        0,
        min(
            float(score or 0),
            100,
        ),
    )

    figure = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "ATS Match Score",
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                },
                "bar": {
                    "thickness": 0.35,
                },
                "steps": [
                    {
                        "range": [0, 50],
                        "color": "#ef4444",
                    },
                    {
                        "range": [50, 75],
                        "color": "#f59e0b",
                    },
                    {
                        "range": [75, 100],
                        "color": "#22c55e",
                    },
                ],
                "threshold": {
                    "line": {
                        "color": "black",
                        "width": 4,
                    },
                    "value": score,
                },
            },
        )
    )

    figure.update_layout(
        height=350,
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
