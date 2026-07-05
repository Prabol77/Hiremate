import os
import streamlit as st


def save_uploaded_file(uploaded_file, upload_dir="uploads"):
    """
    Save the uploaded file locally.

    Args:
        uploaded_file: Streamlit uploaded file object
        upload_dir (str): Directory where files will be saved

    Returns:
        str: Path to the saved file
    """

    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path