from app.ingestion.loader import load_pdf
from app.ingestion.cleaner import clean_text
from app.ingestion.chunker import chunk_text


def ingest_pdf(
        file_path: str,
        chunk_size: int = 1000,
        overlap: int = 200
) -> list[dict]:

    document = load_pdf(file_path)

    all_chunks = []

    for page in document["pages"]:
        cleaned_text = clean_text(page["text"])

        chunks = chunk_text(
            cleaned_text,
            chunk_size=chunk_size,
            overlap=overlap
        )

        for chunk_index, chunk in enumerate(chunks):
            all_chunks.append({
                "document_name": document["document_name"],
                "page_number": page["page_number"],
                "chunk_index": chunk_index,
                "text": chunk
            })

    return all_chunks