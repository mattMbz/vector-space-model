from dataclasses import dataclass

from vsm.exceptions import InvalidLanguageError


@dataclass(frozen=True)
class LanguageConfig:
    name: str
    nltk_name: str
    spacy_model: str


SUPPORTED_LANGUAGES: dict[str, LanguageConfig] = {
    "english": LanguageConfig(
        name="english",
        nltk_name="english",
        spacy_model="en_core_web_sm",
    ),
    "spanish": LanguageConfig(
        name="spanish",
        nltk_name="spanish",
        spacy_model="es_core_news_sm",
    ),
    "portuguese": LanguageConfig(
        name="portuguese",
        nltk_name="portuguese",
        spacy_model="pt_core_news_sm",
    ),
}


def get_language_config(lang: str) -> LanguageConfig:
    normalized_lang = lang.lower().strip()

    try:
        return SUPPORTED_LANGUAGES[normalized_lang]
    except KeyError as exc:
        supported = ", ".join(sorted(SUPPORTED_LANGUAGES))
        raise InvalidLanguageError(
            f"Unsupported language: {lang}. Supported languages: {supported}."
        ) from exc
