# Day 1 Checklist — RAG Fundamentals and Environment

Estimated effort: 3–4 hours.

## Learning objectives

- [ ] Explain what an LLM is and what a hallucination is.
- [ ] Explain Retrieval-Augmented Generation in your own words.
- [ ] Explain the difference between a normal LLM chatbot and a RAG application.
- [ ] Explain the difference between document ingestion and question answering.
- [ ] Explain the role of PyMuPDF, Sentence Transformers, FAISS, Gemini, Streamlit, and Ragas.
- [ ] Draw both pipelines from `architecture.md` by hand or in a diagram tool.

## Dataset preparation

- [ ] Collect 5–10 text-based PDFs that you are allowed to use.
- [ ] Prefer manageable PDFs (approximately 10–100 pages for the first experiment).
- [ ] Check that text can be selected/copied from the PDFs.
- [ ] Record each title, filename, source URL, license/permission, and page count in a local dataset log.
- [ ] Keep the PDFs in `data/raw/`; do not commit files unless redistribution is permitted.

## Environment setup — Windows PowerShell

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/test_environment.py
streamlit hello
```

If activation is blocked in PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

- [ ] Python 3.11 or 3.12 is available.
- [ ] Virtual environment is active (the terminal prompt shows `(.venv)`).
- [ ] Dependencies install without errors.
- [ ] `src/test_environment.py` completes successfully.
- [ ] `streamlit hello` opens the sample application; stop it with Ctrl+C.

## Day 1 knowledge check

Try answering without looking at notes:

1. What are the retrieval and generation parts of RAG?
2. Why do we preserve page numbers and filenames during extraction?
3. Why is a PDF split into chunks before embedding?
4. What does FAISS search, and what does the embedding model produce?
5. Why should the system say when the documents do not contain enough evidence?

## Completion note

Do not mark the environment or dataset tasks complete until you have actually run them locally. Add any errors and their fixes to your project notes.
