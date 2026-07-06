import hashlib

import streamlit as st


class SessionService:
    """
    Manages Streamlit session state.

    Handles:
    - Cached analysis
    - Uploaded file tracking
    """

    ANALYSIS_KEY = "analysis_result"
    FILE_HASH_KEY = "analysis_hash"

    # =====================================================
    # Generate File Hash
    # =====================================================

    def generate_hash(
        self,
        resume_bytes: bytes,
        jd_bytes: bytes,
    ) -> str:
        """
        Generate a unique hash for the uploaded files.
        """

        hasher = hashlib.sha256()

        hasher.update(resume_bytes)

        hasher.update(jd_bytes)

        return hasher.hexdigest()

    # =====================================================
    # Save Analysis
    # =====================================================

    def save_analysis(
        self,
        file_hash: str,
        analysis_result,
    ):
        """
        Save analysis and hash.
        """

        st.session_state[self.ANALYSIS_KEY] = analysis_result

        st.session_state[self.FILE_HASH_KEY] = file_hash

    # =====================================================
    # Check Cache
    # =====================================================

    def has_cached_analysis(
        self,
        file_hash: str,
    ) -> bool:
        """
        Check whether analysis exists
        for the current uploaded files.
        """

        return (
            self.FILE_HASH_KEY in st.session_state
            and st.session_state[self.FILE_HASH_KEY] == file_hash
        )

    # =====================================================
    # Get Analysis
    # =====================================================

    def get_analysis(self):

        return st.session_state.get(self.ANALYSIS_KEY)

    # =====================================================
    # Clear Cache
    # =====================================================

    def clear(self):

        st.session_state.pop(
            self.ANALYSIS_KEY,
            None,
        )

        st.session_state.pop(
            self.FILE_HASH_KEY,
            None,
        )
