"""
ATS Score Gauge.
"""

import plotly.graph_objects as go
import streamlit as st


def render_ats_gauge(
    score: float,
):
    """
    Render ATS gauge.
    """

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text": "ATS Score",
            },

            gauge={

                "axis": {
                    "range": [0, 100],
                },

                "bar": {
                    "thickness": 0.3,
                },

                "steps": [

                    {
                        "range": [0, 50],
                        "color": "#ff6b6b",
                    },

                    {
                        "range": [50, 75],
                        "color": "#ffd166",
                    },

                    {
                        "range": [75, 100],
                        "color": "#06d6a0",
                    },
                ],
            },
        )
    )

    fig.update_layout(
        height=340,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )