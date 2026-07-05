import streamlit as st

from styles.colors import (
    PRIMARY,
    SUCCESS,
    WARNING,
)


def render_kpi_card(
    title: str,
    value: str,
    color: str = PRIMARY,
):
    """
    Render a reusable KPI card.
    """

    st.markdown(
        f"""
<div style="
background:{color};
padding:20px;
border-radius:16px;
color:white;
text-align:center;
box-shadow:0 8px 20px rgba(0,0,0,.12);
">

<h4 style="margin:0;">
{title}
</h4>

<h1 style="margin-top:12px;">
{value}
</h1>

</div>
""",
        unsafe_allow_html=True,
    )