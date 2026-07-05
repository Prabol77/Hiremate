import fitz


def extract_pdf_data(pdf_path: str) -> dict:
    """
    Extract text and metadata from a PDF.

    Args:
        pdf_path (str):
            Path to the PDF file.

    Returns:
        dict:
            {
                "text": str,
                "pages": int,
                "words": int,
                "characters": int
            }
    """

    try:

        doc = fitz.open(pdf_path)

        page_text = []

        for page in doc:
            page_text.append(page.get_text())

        text = "\n".join(page_text).strip()

        pages = len(doc)

        words = len(text.split())

        characters = len(text)

        return {
            "text": text,
            "pages": pages,
            "words": words,
            "characters": characters,
        }

    except Exception as e:

        raise Exception(
            f"Unable to parse PDF: {e}"
        )

    finally:

        try:
            doc.close()
        except Exception:
            pass