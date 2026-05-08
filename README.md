# Vector Space Model

A simple Information Retrieval engine based on the Vector Space Model.

It indexes text documents and runs searches using similarity-based ranking.
Currently supported models:

- TF-IDF
- BM25

## Features

- Small public API through `VectorialEngine`.
- Document ranking by relevance.
- Shared preprocessing pipeline for documents and queries.
- Lowercase normalization.
- Accent removal.
- Tokenization.
- Optional stopword removal.
- Optional stemming.
- Optional lemmatization through spaCy language models.
- Language support for English, Spanish, and Portuguese.
- Tests with `pytest`.

## Installation

```bash
poetry install
```

## Basic Usage

```python
from vsm import VectorialEngine

engine = VectorialEngine(model="tfidf", lang="english")

engine.add_documents(
    {
        "doc1": "python fastapi backend",
        "doc2": "django templates orm",
        "doc3": "python boolean search engine",
    }
)

results = engine.search("I need Django and Fastapi documentation")

for result in results:
    print(result.doc_id, result.score, result.text)
```

## Available Models

```python
VectorialEngine(model="tfidf")
VectorialEngine(model="bm25")
```

## Text Processing

`stopwords`, `stemming`, and `lemmatizer` are disabled by default.

```python
engine = VectorialEngine(
    model="tfidf",
    lang="english",
    stopwords=True,
    stemming=True,
    lemmatizer=False,
)
```

The same pipeline is applied to both documents and queries.

Supported languages:

- `english`
- `spanish`
- `portuguese`

Stopwords and stemming use NLTK. If stopwords are enabled, install the NLTK
corpus once:

```bash
poetry run python -m nltk.downloader stopwords
```

Lemmatization requires the matching spaCy model for the selected language.

## Main Structure

```text
vsm/
├── engine.py
├── models/
│   ├── tfidf_model.py
│   └── bm25_model.py
├── text_processing/
│   ├── normalizer.py
│   ├── tokenizer.py
│   ├── stopwords.py
│   ├── stemmer.py
│   ├── lemmatizer.py
│   ├── languages.py
│   └── processor.py
├── result.py
└── exceptions.py
```

## Tests

```bash
poetry run pytest
```
