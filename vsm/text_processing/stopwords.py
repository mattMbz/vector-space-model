from nltk.corpus import stopwords

from vsm.exceptions import MissingLanguageResourceError
from vsm.text_processing.languages import LanguageConfig
from vsm.text_processing.normalizer import TextNormalizer


class StopWordsRemover:
    def __init__(self, language: LanguageConfig) -> None:
        self.language = language
        self.normalizer = TextNormalizer()
        self.stopwords = self._load_stopwords()

    def remove(self, tokens: list[str]) -> list[str]:
        return [token for token in tokens if token not in self.stopwords]

    def _load_stopwords(self) -> set[str]:
        try:
            return {
                self.normalizer.normalize(word)
                for word in stopwords.words(self.language.nltk_name)
            }
        except LookupError as exc:
            raise MissingLanguageResourceError(
                "Missing NLTK stopwords corpus. "
                "Run: python -m nltk.downloader stopwords"
            ) from exc
