import streamlit as st

EXCELLENT_THRESHOLD = 85
STRONG_THRESHOLD = 70
MODERATE_THRESHOLD = 50


def render_ats_card(
    score: float,
) -> None:
    """
    Render the ATS compatibility card.

    Args:
        score:
            ATS compatibility score (0-100).
    """

    # ------------------------------------------
    # Normalize Score
    # ------------------------------------------

    if score is None:
        score = 0.0

    score = max(0.0, min(float(score), 100.0))

    # ------------------------------------------
    # Header
    # ------------------------------------------

    st.subheader("🎯 ATS Match")

    # ------------------------------------------
    # Score
    # ------------------------------------------

    st.metric(
        "Compatibility",
        f"{score:.1f}%",
    )

    st.progress(score / 100)

    # ------------------------------------------
    # Match Status
    # ------------------------------------------

    if score >= EXCELLENT_THRESHOLD:

        st.success("Excellent Match")

    elif score >= STRONG_THRESHOLD:

        st.info("Strong Match")

    elif score >= MODERATE_THRESHOLD:

        st.warning("Moderate Match")

    else:

        st.error("Low Match")
