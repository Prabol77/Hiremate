"""
Skills Donut Chart.
"""

import plotly.graph_objects as go
import streamlit as st


def render_skills_donut(
    matched: int,
    missing: int,
):
    """
    Render skills match donut chart.
    """

    fig = go.Figure(
        data=[
            go.Pie(
                labels=[
                    "Matched",
                    "Missing",
                ],
                values=[
                    matched,
                    missing,
                ],
                hole=0.65,
                textinfo="label+percent",
            )
        ]
    )

    fig.update_layout(

        title="📊 Skills Match",

        height=340,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),

        showlegend=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )