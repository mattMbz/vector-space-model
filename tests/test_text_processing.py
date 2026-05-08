import pytest

from vsm import VectorialEngine
from vsm.exceptions import InvalidLanguageError
from vsm.text_processing import TextProcessor


def test_processor_normalizes_and_tokenizes_by_default():
    processor = TextProcessor(lang="spanish")

    assert processor.process("Python, información rápida!") == [
        "python",
        "informacion",
        "rapida",
    ]


def test_processor_removes_english_stopwords_when_enabled():
    processor = TextProcessor(lang="english", stopwords=True)

    assert processor.process("python and fastapi para backend") == [
        "python",
        "fastapi",
        "para",
        "backend",
    ]


def test_processor_removes_spanish_stopwords_when_enabled():
    processor = TextProcessor(lang="spanish", stopwords=True)

    assert processor.process("python y fastapi para más backend") == [
        "python",
        "fastapi",
        "backend",
    ]


def test_processor_removes_portuguese_stopwords_when_enabled():
    processor = TextProcessor(lang="portuguese", stopwords=True)

    assert processor.process("python e fastapi para backend") == [
        "python",
        "fastapi",
        "backend",
    ]


def test_processor_applies_stemming_when_enabled():
    processor = TextProcessor(lang="english", stemming=True)

    assert processor.process("running searches documents") == [
        "run",
        "search",
        "document",
    ]


def test_processor_rejects_unsupported_language():
    with pytest.raises(InvalidLanguageError):
        TextProcessor(lang="italian")


@pytest.mark.parametrize(
    ("lang", "text"),
    [
        ("english", "dogs are running"),
        ("spanish", "los perros corren"),
        ("portuguese", "os cachorros correm"),
    ],
)
def test_processor_loads_lemmatizer_for_supported_languages(lang, text):
    processor = TextProcessor(lang=lang, lemmatizer=True)

    assert processor.process(text)


def test_tfidf_engine_uses_configured_text_processing():
    engine = VectorialEngine(
        model="tfidf",
        lang="english",
        stopwords=True,
        stemming=True,
    )
    engine.add_documents(
        {
            "doc1": "running backend services",
            "doc2": "frontend template",
            "doc3": "database schema",
        }
    )

    result = engine.search("run and service")

    assert result[0].doc_id == "doc1"


def test_bm25_engine_uses_configured_text_processing():
    engine = VectorialEngine(
        model="bm25",
        lang="english",
        stopwords=True,
        stemming=True,
    )
    engine.add_documents(
        {
            "doc1": "running backend services",
            "doc2": "frontend template",
            "doc3": "database schema",
        }
    )

    result = engine.search("run and service")

    assert result[0].doc_id == "doc1"
