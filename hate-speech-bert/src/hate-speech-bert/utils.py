"""
Utility helpers for Hate speech BERT.
"""
from pathlib import Path
import pandas as pd

def load_data(filename: str = "ucberkeley-dlab/measuring-hate-speech (HuggingFace)") -> pd.DataFrame:
    """Load CSV from data/ folder."""
    path = Path("data") / filename
    return pd.read_csv(path)
