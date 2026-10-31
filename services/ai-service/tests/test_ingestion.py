from app.ingestion.cleaner import clean_text
from app.ingestion.chunker import chunk_text
from app.ingestion.pipeline import ingest_pdf

def test_clean_text():
    result = clean_text("Hello    world\n\nAI")
    assert result == "Hello world AI"


def test_chunk_text():
    text = "A" * 2500

    chunks = chunk_text(
        text,
        chunk_size=1000,
        overlap=200
    )

    assert len(chunks) == 4
    assert len(chunks[0]) == 1000
    assert len(chunks[1]) == 1000
    assert len(chunks[2]) == 900
    assert len(chunks[3]) == 100


def test_invalid_overlap():
    try:
        chunk_text("Hello", chunk_size=100, overlap=100)
        assert False
    except ValueError:
        assert True
        from app.ingestion.pipeline import ingest_pdf


def test_ingest_pdf(tmp_path):
    import fitz

    pdf_path = tmp_path / "sample.pdf"

    document = fitz.open()
    page = document.new_page()
    page.insert_text(
        (50, 50),
        "This is a sample research document about artificial intelligence."
    )
    document.save(pdf_path)
    document.close()

    chunks = ingest_pdf(str(pdf_path))

    assert len(chunks) > 0
    assert chunks[0]["document_name"] == "sample.pdf"
    assert chunks[0]["page_number"] == 1
    assert "artificial intelligence" in chunks[0]["text"]