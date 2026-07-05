import streamlit as st


def show_about():

    st.title("About HireMate")

    st.markdown(
        """
### HireMate

An AI-powered Resume & Job Matching Platform.

### Current Features

- Resume Upload
- Resume Parsing
- Resume Preview

### Upcoming Features

- ATS Score
- Skill Matching
- Resume Optimization
- AI Interview Questions
- Learning Roadmap
- Cover Letter Generator
"""
    )