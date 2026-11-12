"""Basic Day 1 environment smoke test.

Run from the project root with the project virtual environment activated:
    python src/test_environment.py
"""

from __future__ import annotations

import sys


def main() -> int:
    try:
        import fitz
        import numpy as np
        import pandas as pd
        import streamlit as st
    except ImportError as exc:
        print(f"A required dependency is missing: {exc}")
        print("Activate the project virtual environment and run: pip install -r requirements.txt")
        return 1

    print("Python environment is working!")
    print(f"Python: {sys.version.split()[0]}")
    print(f"PyMuPDF: {fitz.VersionBind}")
    print(f"Pandas: {pd.__version__}")
    print(f"NumPy: {np.__version__}")
    print(f"Streamlit: {st.__version__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
