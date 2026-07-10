"""
HireMate Design System.
"""

import streamlit as st


def section(title: str, subtitle: str = ""):
    st.subheader(title)

    if subtitle:
        st.caption(subtitle)


def success(message: str):
    st.success(message)


def warning(message: str):
    st.warning(message)


def error(message: str):
    st.error(message)


def info(message: str):
    st.info(message)


def divider():
    st.divider()