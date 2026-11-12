# PDF Question-Answering Chatbot using Retrieval-Augmented Generation (RAG)

A student project to help users ask natural-language questions about information contained in their PDF documents. The planned system extracts text from PDFs, cleans and chunks it, generates sentence embeddings, retrieves relevant passages with vector similarity search, and uses an LLM to create grounded answers with document and page references.

> **Current stage: Day 1 – planning and environment setup.** Repository documentation and starter files are prepared. The local Python environment, actual PDF collection, and runtime checks still need to be completed on the developer's computer.

## Problem statement
Students, researchers, and professionals often spend significant time searching long textbooks, research papers, technical manuals, and reports for specific information. This project aims to make that process easier by allowing users to ask questions in natural language and receive answers grounded in uploaded documents, together with source references that can be checked.

## Project objectives
- Accept multiple PDF documents as a knowledge source.
- Extract text page by page while retaining document and page metadata.
- Clean extracted text and split it into manageable, overlapping chunks.
- Generate dense text embeddings for document chunks and questions.
- Retrieve relevant chunks using vector similarity search.
- Use a Large Language Model (LLM) with retrieved context to produce grounded answers.
- Display source document names and page numbers alongside answers.
- Evaluate retrieval quality using Precision@K, Recall@K, and Mean Reciprocal Rank (MRR).

## Planned architecture

### Document ingestion pipeline
```text
PDF files
   -> Page-wise text extraction
   -> Text preprocessing
   -> Chunking and metadata attachment
   -> Sentence embeddings
   -> Vector index (FAISS) + chunk metadata
```

### Question-answering pipeline
```text
User question
   -> Question embedding
   -> Similarity search in FAISS
   -> Top-K relevant chunks
   -> Prompt/context construction
   -> Gemini LLM generation
   -> Answer with document/page references
```

The ingestion path is run when documents are added or re-indexed. The question-answering path is run for each user query. The LLM should be instructed to use the retrieved context and say when the documents do not contain enough information. This can reduce unsupported answers, but does not guarantee that hallucinations are eliminated.

## Initial technology choices

| Component | Initial choice | Purpose |
|---|---|---|
| Programming language | Python | Main implementation language |
| PDF extraction | PyMuPDF | Extract page-wise PDF text |
| Data handling | NumPy, Pandas, Python `re` | Basic processing and analysis |
| Embeddings | Sentence Transformers | Convert text into dense vectors |
| Baseline embedding model | `all-MiniLM-L6-v2` | Initial sentence-embedding baseline |
| Vector search | FAISS (`faiss-cpu`) | Retrieve nearest vectors efficiently |
| Answer generation | Gemini API (`google-genai`) | Generate answers using retrieved context |
| Interface | Streamlit | Build the user-facing app |
| Evaluation | Custom retrieval metrics; Ragas as an additional tool | Evaluate retrieval and generation separately |

These are starting choices, not claims that they are optimal. Model choice, chunk size, overlap, and retrieval settings should be compared experimentally during development.

## Repository structure

```text
pdf-rag-chatbot/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── raw/                 # Local source PDFs; not committed
│   └── processed/           # Local extracted/chunked data; not committed
├── docs/
│   ├── architecture.md
│   └── day-01-checklist.md
├── src/
│   ├── __init__.py
│   ├── test_environment.py
│   ├── pdf_loader.py
│   ├── preprocessing.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── rag_pipeline.py
│   └── evaluation.py
├── tests/
├── vectorstore/             # Local vector index; not committed
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Local setup (Windows PowerShell)

Python 3.11 or 3.12 is recommended for a predictable package setup.

```powershell
git clone https://github.com/agrawalabhi881-a11y/pdf-rag-chatbot.git
cd pdf-rag-chatbot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/test_environment.py
```

If PowerShell blocks virtual-environment activation, run this in the current terminal and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

To run the Streamlit sample check:

```powershell
streamlit hello
```

Stop the sample server with `Ctrl+C`.

## Environment variables and API keys

Copy `.env.example` to `.env` when API integration begins, then add your own Gemini API key. Day 1 does not require an API key. Never commit `.env`, API keys, private documents, or generated vector indexes.

## Dataset plan

For the first experiment, collect 5–10 text-based PDFs such as course notes, openly licensed textbooks, public technical reports, or research papers whose use is permitted. Start with manageable files (for example, 10–100 pages). Avoid password-protected PDFs and scanned documents in the first version because scanned PDFs may require OCR.

Keep a local dataset log containing:
- Document title and filename
- Source URL or citation
- License/permission notes
- Page count
- Whether the PDF contains selectable text

Do not commit copyrighted PDFs unless the license explicitly permits redistribution.

## Evaluation plan

Create a small test set of questions and manually label which chunks are relevant to each question.

- **Precision@K:** number of relevant chunks in the top K results divided by K.
- **Recall@K:** number of relevant chunks in the top K results divided by the total number of relevant chunks for that query.
- **MRR:** average reciprocal rank of the first relevant result across the query set.

These are retrieval metrics. Evaluate generated answer quality separately, for example with faithfulness (support from retrieved context), answer relevance, and human review. A good retrieval score alone does not prove that the final answer is correct.

## 10-day execution outline

1. RAG fundamentals, architecture, dataset selection, and environment setup.
2. PDF extraction and text preprocessing.
3. Text chunking and metadata handling.
4. Sentence embedding generation.
5. FAISS indexing and semantic retrieval.
6. Basic RAG pipeline.
7. Gemini integration and grounded answer generation.
8. Retrieval and answer evaluation.
9. Streamlit interface.
10. Integration, testing, and documentation.

## Day 1 status

- [x] Project scope and initial technology choices documented.
- [x] Document-ingestion architecture documented.
- [x] Question-answering architecture documented.
- [x] Local setup instructions and starter folder structure prepared.
- [ ] Collect 5–10 suitable sample PDFs locally and record their sources.
- [ ] Create and activate the local Python virtual environment.
- [ ] Install dependencies and run `src/test_environment.py` locally.
- [ ] Read the Day 1 fundamentals and complete the checklist.

The checked boxes describe files prepared in this scaffold. The unchecked items require work on the developer's computer; they have not been run or verified here.
