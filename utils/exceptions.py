class ResumeParsingError(Exception):
    """Raised when a resume cannot be parsed."""


class UnsupportedFileError(Exception):
    """Raised when the uploaded file type is unsupported."""