from pathlib import Path
import fitz


def load_pdf(file_path: str) -> dict:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported")

    document = fitz.open(path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text")

        if text.strip():
            pages.append({
                "page_number": page_number,
                "text": text
            })

    document.close()

    return {
        "document_name": path.name,
        "total_pages": len(pages),
        "pages": pages
    }