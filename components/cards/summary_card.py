import streamlit as st


def render_summary_card(result):

    matched = len(result.matched_skills)

    missing = len(result.missing_skills)

    additional = len(result.additional_skills)

    c1, c2, c3 = st.columns(3)

    c1.metric("Matched", matched)

    c2.metric("Missing", missing)

    c3.metric("Extra", additional)