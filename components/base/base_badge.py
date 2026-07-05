import streamlit as st


def render_badge(
    text: str,
    color: str = "#2563EB",
):
    """
    Render a reusable badge.
    """

    st.markdown(
        f"""
<span
style="
background:{color};
color:white;
padding:6px 14px;
border-radius:999px;
font-size:14px;
font-weight:600;
display:inline-block;
margin:4px;
">
{text}
</span>
""",
        unsafe_allow_html=True,
    )