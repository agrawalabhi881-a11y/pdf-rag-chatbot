# System Architecture

## 1. Project overview

The proposed application answers natural-language questions using content from PDFs uploaded by a user. Retrieval-Augmented Generation (RAG) connects an information-retrieval component to a language-generation component: the retriever finds relevant source passages and the LLM uses those passages as context when composing an answer.

## 2. Document ingestion pipeline

1. **PDF input:** accept one or more PDF files.
2. **Text extraction:** extract text page by page with PyMuPDF. Keep the source filename and one-based page number.
3. **Preprocessing:** normalize whitespace and remove extraction artefacts carefully. Do not strip meaningful symbols, headings, equations, or punctuation indiscriminately.
4. **Chunking:** split page text into smaller passages, with configurable chunk size and overlap. Preserve source metadata for every chunk.
5. **Embedding:** encode each chunk using a sentence-embedding model.
6. **Indexing:** add vectors to a FAISS index and store a mapping from vector IDs to chunk text and metadata.

Suggested chunk metadata:

```python
{
    "chunk_id": "doc-001-page-12-chunk-03",
    "document_name": "machine_learning_notes.pdf",
    "page_number": 12,
    "text": "..."
}
```

## 3. Question-answering pipeline

1. Receive the user's question.
2. Encode the question with the same embedding model used for document chunks.
3. Search the FAISS index for the nearest vectors.
4. Retrieve the corresponding chunk text and metadata.
5. Build a prompt containing the question, retrieved evidence, and instructions to avoid unsupported claims.
6. Send the prompt to the Gemini API.
7. Present the answer with source document and page references.

If the retrieved passages do not contain enough evidence, the application should say that the answer could not be found in the uploaded documents rather than inventing a response.

## 4. Initial technology choices

- Python for application logic.
- PyMuPDF for PDF text extraction.
- Sentence Transformers for dense text embeddings.
- FAISS for vector similarity search.
- Gemini API for response generation.
- Streamlit for the interface.

The initial embedding model is `all-MiniLM-L6-v2`. It is a baseline for experimentation, not a pre-established best model for this dataset.

## 5. Evaluation

For each evaluation question, create a ground-truth set of relevant chunks. Calculate Precision@K, Recall@K, and MRR for retrieval. Evaluate answer faithfulness and relevance separately. Record the dataset, question set, K value, embedding model, chunk configuration, and retrieval settings so experiments can be compared fairly.

## 6. Known limitations to consider

- Scanned/image-only PDFs may need OCR, which is outside the first version.
- Tables, mathematical equations, multi-column layouts, and unusual fonts can extract poorly.
- Chunk boundaries may separate related ideas.
- Similarity search can retrieve passages that are semantically close but not sufficient to answer the question.
- LLM answers may still be incomplete or incorrect; citations and evaluation are important, but are not guarantees.
