# Hate speech BERT

By integrating BERT with NLP techniques, the model is designed to not only identify hate speech but also to understand its various dimensions and contexts.

## Quickstart

```bash
# Create project from template
cookiecutter path/to/this/template

# cd into project
cd hate-speech-bert

# Create env (optional) and install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

## Structure

```
hate-speech-bert/
├── data/                      # put your datasets here (default: ucberkeley-dlab/measuring-hate-speech (HuggingFace))
├── notebooks/
│   └── BERT.ipynb
├── src/hate-speech-bert/
│   ├── __init__.py
│   └── utils.py
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Notes

- This starter targets **Jupyter notebooks** using **panel** stack (Panel/Plotly/Seaborn).
- Replace sample paths with your real dataset names (default is ucberkeley-dlab/measuring-hate-speech (HuggingFace)).
