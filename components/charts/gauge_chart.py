import plotly.graph_objects as go

import streamlit as st


def render_gauge(score: float):
    """
    ATS Gauge Chart.
    """

    figure = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text": "ATS Match Score"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "thickness": 0.35
                },

                "steps": [

                    {
                        "range": [0, 50],
                        "color": "#ef4444"
                    },

                    {
                        "range": [50, 75],
                        "color": "#f59e0b"
                    },

                    {
                        "range": [75, 100],
                        "color": "#22c55e"
                    }

                ]
            }

        )
    )

    figure.update_layout(
        height=350,
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
    )