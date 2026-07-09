"""
Premium metric card component.
"""

import streamlit as st


def render_metric_card_v2(
    *,
    title: str,
    value: str,
    subtitle: str = "",
    icon: str = "📊",
):
    """
    Render a premium dashboard metric card.
    """

    st.markdown(
        f"""
<div style="
background:#1E1E1E;
padding:20px;
border-radius:16px;
border:1px solid #303030;
text-align:center;
height:170px;
">

<div style="font-size:32px">
{icon}
</div>

<div style="
font-size:15px;
color:#BFBFBF;
margin-top:10px;
">
{title}
</div>

<div style="
font-size:36px;
font-weight:bold;
margin-top:10px;
">
{value}
</div>

<div style="
color:#7FD67F;
margin-top:10px;
">
{subtitle}
</div>

</div>
""",
        unsafe_allow_html=True,
    )