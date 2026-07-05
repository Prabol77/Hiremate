import plotly.graph_objects as go

import streamlit as st


def render_resume_strength():

    figure = go.Figure()

    figure.add_trace(

        go.Scatterpolar(

            r=[80, 65, 70, 75, 60],

            theta=[
                "Skills",
                "Projects",
                "Experience",
                "Education",
                "Certifications",
            ],

            fill="toself",
        )

    )

    figure.update_layout(

        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
            )
        ),

        showlegend=False,

        height=400,
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
    )