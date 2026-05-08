from vsm.exceptions import MissingLanguageResourceError
from vsm.text_processing.languages import LanguageConfig


class Lemmatizer:
    def __init__(self, language: LanguageConfig) -> None:
        self.language = language
        self._nlp = self._load_model()

    def lemmatize_tokens(self, tokens: list[str]) -> list[str]:
        doc = self._nlp(" ".join(tokens))
        return [token.lemma_.lower() for token in doc if token.lemma_]

    def _load_model(self):
        try:
            import spacy
        except ImportError as exc:
            raise MissingLanguageResourceError(
                "spaCy is required when lemmatizer=True."
            ) from exc

        try:
            return spacy.load(
                self.language.spacy_model,
                disable=["parser", "ner"],
            )
        except OSError as exc:
            raise MissingLanguageResourceError(
                "Missing spaCy model for "
                f"{self.language.name}: {self.language.spacy_model}. "
                f"Install it before using lemmatizer=True."
            ) from exc
