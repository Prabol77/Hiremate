import streamlit as st


def render_ats_card(score: float):
    """
    Render ATS score card.
    """

    st.subheader("🎯 ATS Match")

    st.metric(
        "Compatibility",
        f"{score:.1f}%"
    )

    st.progress(score / 100)

    if score >= 85:

        st.success("Excellent Match")

    elif score >= 70:

        st.info("Strong Match")

    elif score >= 50:

        st.warning("Moderate Match")

    else:

        st.error("Low Match")