"""
HireMate Application Entry Point.
"""

import streamlit as st

from components.layout.sidebar import render_sidebar
from styles.theme import load_theme

from views.product_info import (
    show_product_info,
)
from views.dashboard import show_dashboard



def main():
    """
    Configure and launch the HireMate application.
    """

    st.set_page_config(
        page_title="HireMate",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    load_theme()

    page = render_sidebar()

    if page == "🏠 Dashboard":

        show_dashboard()

    else:

        show_product_info()

if __name__ == "__main__":
    main()
