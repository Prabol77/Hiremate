import os
import uuid
from pathlib import Path

from streamlit.runtime.uploaded_file_manager import UploadedFile


def save_uploaded_file(
    uploaded_file: UploadedFile,
    upload_dir: str = "uploads",
) -> str:
    """
    Save an uploaded file safely.

    Args:
        uploaded_file:
            Streamlit uploaded file.

        upload_dir:
            Directory used to store uploaded files.

    Returns:
        str:
            Absolute path to the saved file.

    Raises:
        ValueError:
            If no file is provided.

        IOError:
            If the file cannot be written.
    """

    if uploaded_file is None:
        raise ValueError("No uploaded file provided.")

    os.makedirs(
        upload_dir,
        exist_ok=True,
    )

    extension = Path(uploaded_file.name).suffix.lower()

    unique_filename = f"{uuid.uuid4().hex}{extension}"

    file_path = os.path.join(
        upload_dir,
        unique_filename,
    )

    try:

        with open(
            file_path,
            "wb",
        ) as file:

            file.write(uploaded_file.getbuffer())

    except OSError as exc:

        raise IOError(f"Unable to save uploaded file: {exc}") from exc

    return file_path
