import streamlit as st


class ProgressPipeline:
    """
    Professional progress pipeline for HireMate.
    """

    def __init__(self) -> None:
        """
        Initialize the progress widgets.
        """

        self.progress = st.progress(0)

        self.status = st.empty()

    # =====================================================
    # Update Progress
    # =====================================================

    def update(
        self,
        value: int,
        message: str,
    ) -> None:
        """
        Update progress and status message.
        """

        value = max(0, min(value, 100))

        self.progress.progress(value)

        self.status.info(message)

    # =====================================================
    # Finish
    # =====================================================

    def finish(self) -> None:
        """
        Mark the pipeline as completed.
        """

        self.progress.progress(100)

        self.status.success("✅ Analysis completed successfully!")

    # =====================================================
    # Error
    # =====================================================

    def error(
        self,
        message: str,
    ) -> None:
        """
        Display an error message.
        """

        self.status.error(message)

    # =====================================================
    # Reset
    # =====================================================

    def reset(self) -> None:
        """
        Reset the progress pipeline.
        """

        self.progress.progress(0)

        self.status.empty()
