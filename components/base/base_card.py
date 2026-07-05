import streamlit as st


def render_base_card(
    title: str,
    body: str = "",
    icon: str = "",
):
    """
    Render a reusable HireMate card.
    """

    st.markdown(
        f"""
<div style="
background:white;
padding:22px;
border-radius:18px;
border:1px solid #E5E7EB;
box-shadow:0 8px 20px rgba(0,0,0,.05);
margin-bottom:18px;
">

<h3 style="margin-bottom:12px;">
{icon} {title}
</h3>

{body}

</div>
""",
        unsafe_allow_html=True,
    )